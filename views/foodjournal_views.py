from flask import Blueprint, request, redirect, render_template, url_for
from flask.views import MethodView
from flask.ext.mongoengine.wtf import model_form
from weighttracker.models.foodjournal import Foodjournal

foodjournals = Blueprint('foodjournals', __name__, template_folder='templates')


class ListFoodjournals(MethodView):

  def get(self, page=1):
    foodjournals = Foodjournal.objects.paginate(page, per_page=10)
    return render_template('foodjournals/list.html', foodjournals=foodjournals)


class ShowFoodjournal(MethodView):

  def get(self, eating_time):
    foodjournal = Foodjournal.objects.get_or_404(eating_time=eating_time )
    return render_template('foodjournals/show.html', foodjournal=foodjournal)


class EditFoodjournal(MethodView):

  def get(self, eating_time):
    foodjournal = Foodjournal.objects.get_or_404(eating_time=eating_time )
    return render_template('foodjournals/edit.html', foodjournal=foodjournal)


class NewFoodjournal(MethodView):

  def get_context(self, eating_time=None):
    form_cls = model_form(Foodjournal, exclude=('created_at', 'updated_at'))

    if eating_time:
      foodjournal = Foodjournal.objects.get_or_404(eating_time=eating_time)
      if request.method == 'POST':
        form = form_cls(request.form, inital=foodjournal._data)
      else:
        form = form_cls(obj=foodjournal)
    else:
      foodjournal = Foodjournal()
      form = form_cls(request.form)

    context = {
            "foodjournal": foodjournal,
            "form": form,
            "create": eating_time is None
    }

    return context


  def get(self, eating_time=None):
    context = self.get_context(eating_time)
    return render_template('foodjournals/new.html', **context)

  def post(self, eating_time=None):
    context = self.get_context(eating_time)
    form = context.get('form')

    if form.valieating_time():
      foodjournal = context.get('foodjournal')
      form.populate_obj(foodjournal)
      foodjournal.save()

      return redirect(url_for('foodjournals.list'))
    return render_template('foodjournals/new.html', **context)



# Register the urls
foodjournals.add_url_rule('/foodjournals/', view_func=ListFoodjournals.as_view('list'))
foodjournals.add_url_rule('/foodjournals/<int:page>/', view_func=ListFoodjournals.as_view('listpage'))
foodjournals.add_url_rule('/foodjournals/new/', view_func=NewFoodjournal.as_view('new'))
foodjournals.add_url_rule('/foodjournals/create/', defaults={'eating_time': None}, view_func=NewFoodjournal.as_view('create'))
foodjournals.add_url_rule('/foodjournals/<eating_time>/', view_func=ShowFoodjournal.as_view('show'))
foodjournals.add_url_rule('/foodjournals/edit/<eating_time>/', view_func=NewFoodjournal.as_view('edit'))