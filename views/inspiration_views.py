from flask import Blueprint, request, redirect, render_template, url_for
from flask.views import MethodView
from flask.ext.mongoengine.wtf import model_form
from weighttracker.models.inspiration import Inspiration

inspirations = Blueprint('inspirations', __name__, template_folder='templates')


class ListInspirations(MethodView):

  def get(self):
    inspirations = Inspiration.objects.all()
    return render_template('inspirations/list.html', inspirations=inspirations)



class ShowInspiration(MethodView):

  def get(self, phrase):
    inspiration = Inspiration.objects.get_or_404(phrase=phrase )
    return render_template('inspirations/show.html', inspiration=inspiration)


class EditInspiration(MethodView):

  def get(self, phrase):
    inspiration = Inspiration.objects.get_or_404(phrase=phrase )
    return render_template('inspirations/edit.html', inspiration=inspiration)


class NewInspiration(MethodView):

  def get_context(self, phrase=None):
    form_cls = model_form(Inspiration, exclude=('created_at', 'updated_at'))

    if phrase:
      inspiration = Inspiration.objects.get_or_404(phrase=phrase)
      if request.method == 'POST':
        form = form_cls(request.form, inital=inspiration._data)
      else:
        form = form_cls(obj=inspiration)
    else:
      inspiration = Inspiration()
      form = form_cls(request.form)

    context = {
            "inspiration": inspiration,
            "form": form,
            "create": phrase is None
    }

    return context


  def get(self, phrase=None):
    context = self.get_context(phrase)
    return render_template('inspirations/new.html', **context)

  def post(self, phrase=None):
    context = self.get_context(phrase)
    form = context.get('form')

    if form.validate():
      inspiration = context.get('inspiration')
      form.populate_obj(inspiration)
      inspiration.save()

      return redirect(url_for('inspirations.list'))
    return render_template('inspirations/new.html', **context)



# Register the urls
inspirations.add_url_rule('/inspirations/', view_func=ListInspirations.as_view('list'))
inspirations.add_url_rule('/inspirations/new/', view_func=NewInspiration.as_view('new'))
inspirations.add_url_rule('/inspirations/create/', defaults={'phrase': None}, view_func=NewInspiration.as_view('create'))
inspirations.add_url_rule('/inspirations/<phrase>/', view_func=ShowInspiration.as_view('show'))
inspirations.add_url_rule('/inspirations/edit/<phrase>/', view_func=NewInspiration.as_view('edit'))