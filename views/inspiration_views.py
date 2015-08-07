from flask import Blueprint, request, redirect, render_template, url_for
from flask.views import MethodView
from flask.ext.mongoengine.wtf import model_form
from weighttracker.models.inspiration import Inspiration
from datetime import datetime

inspirations = Blueprint('inspirations', __name__, template_folder='templates')


class ListInspirations(MethodView):

  def get(self, page=1):
    inspirations = Inspiration.objects.paginate(page, per_page=10)
    return render_template('inspirations/list.html', inspirations=inspirations)


class ShowInspiration(MethodView):

  def get(self, id):
    inspiration = Inspiration.objects.get_or_404(id=id )
    return render_template('inspirations/show.html', inspiration=inspiration)


class EditInspiration(MethodView):

  def get(self, id):
    inspiration = Inspiration.objects.get_or_404(id=id )
    header_text = "Edit This Inspiration"
    return render_template('inspirations/edit.html', inspiration=inspiration, header_text=header_text)


class NewInspiration(MethodView):

  def get_context(self, id=None):
    form_cls = model_form(Inspiration, exclude=('created_at', 'updated_at'))

    if id:
      inspiration = Inspiration.objects.get_or_404(id=id)
      header_text = "Edit This Inspiration"
      if request.method == 'POST':
        form = form_cls(request.form, inital=inspiration._data)
      else:
        form = form_cls(obj=inspiration)
    else:
      inspiration = Inspiration()
      header_text = "Add a New Inspiration"
      form = form_cls(request.form)

    context = {
            "inspiration": inspiration,
            "form": form,
            "header_text": header_text,
            "create": id is None
    }

    return context


  def get(self, id=None):
    context = self.get_context(id)
    return render_template('inspirations/new.html', **context)

  def post(self, id=None):
    context = self.get_context(id)
    form = context.get('form')

    if form.validate():
      inspiration = context.get('inspiration')
      form.populate_obj(inspiration)

      # Update the updated_at field
      inspiration['updated_at'] = datetime.now()

      inspiration.save()

      return redirect(url_for('inspirations.list'))
    return render_template('inspirations/new.html', **context)



# Register the urls
inspirations.add_url_rule('/inspirations/', view_func=ListInspirations.as_view('list'))
inspirations.add_url_rule('/inspirations/<int:page>/', view_func=ListInspirations.as_view('listpage'))
inspirations.add_url_rule('/inspirations/new/', view_func=NewInspiration.as_view('new'))
inspirations.add_url_rule('/inspirations/create/', defaults={'id': None}, view_func=NewInspiration.as_view('create'))
inspirations.add_url_rule('/inspirations/<id>/', view_func=ShowInspiration.as_view('show'))
inspirations.add_url_rule('/inspirations/edit/<id>/', view_func=NewInspiration.as_view('edit'))