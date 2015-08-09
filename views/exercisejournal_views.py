from flask import Blueprint, request, redirect, render_template, url_for
from flask.views import MethodView
from flask.ext.mongoengine.wtf import model_form
from weighttracker.models.exercisejournal import Exercisejournal
import parsedatetime
from datetime import datetime
from time import mktime

exercisejournals = Blueprint('exercisejournals', __name__, template_folder='templates')


class ListExercisejournals(MethodView):

  def get(self, page=1):
    exercisejournals = Exercisejournal.objects.order_by('-exercise_time_parsed').paginate(page, per_page=10)
    return render_template('exercisejournals/list.html', exercisejournals=exercisejournals)


class ShowExercisejournal(MethodView):

  def get(self, id):
    exercisejournal = Exercisejournal.objects.get_or_404(id=id )
    return render_template('exercisejournals/show.html', exercisejournal=exercisejournal)


class EditExercisejournal(MethodView):

  def get(self, id):
    exercisejournal = Exercisejournal.objects.get_or_404(id=id )
    header_text = "Edit This Exercise Journal Entry"
    return render_template('exercisejournals/edit.html', exercisejournal=exercisejournal, header_text=header_text)


class NewExercisejournal(MethodView):

  def get_context(self, id=None):
    form_cls = model_form(Exercisejournal, exclude=('created_at', 'updated_at'))

    if id:
      exercisejournal = Exercisejournal.objects.get_or_404(id=id)
      header_text = "Edit This Exercise Journal Entry"
      if request.method == 'POST':
        form = form_cls(request.form, inital=exercisejournal._data)
      else:
        form = form_cls(obj=exercisejournal)
    else:
      exercisejournal = Exercisejournal()
      header_text = "Add a New Exercise Journal Entry"
      form = form_cls(request.form)

    context = {
            "exercisejournal": exercisejournal,
            "form": form,
            "header_text": header_text,
            "create": id is None
    }

    return context


  def get(self, id=None):
    context = self.get_context(id)
    return render_template('exercisejournals/new.html', **context)

  def post(self, id=None):
    context = self.get_context(id)
    form = context.get('form')

    if form.validate():
      exercisejournal = context.get('exercisejournal')
      form.populate_obj(exercisejournal)

      # Add the eating_time_parsed value, or update it
      cal = parsedatetime.Calendar()
      time_struct, parse_status = cal.parse(exercisejournal['exercise_time'])
      exercisejournal['exercise_time_parsed'] = datetime.fromtimestamp(mktime(time_struct))
      exercisejournal['updated_at'] = datetime.now()

      # Save the record
      exercisejournal.save()

      return redirect(url_for('exercisejournals.list'))
    return render_template('exercisejournals/new.html', **context)



# Register the urls
exercisejournals.add_url_rule('/exercisejournals/', view_func=ListExercisejournals.as_view('list'))
exercisejournals.add_url_rule('/exercisejournals/<int:page>/', view_func=ListExercisejournals.as_view('listpage'))
exercisejournals.add_url_rule('/exercisejournals/new/', view_func=NewExercisejournal.as_view('new'))
exercisejournals.add_url_rule('/exercisejournals/create/', defaults={'exercise_time': None}, view_func=NewExercisejournal.as_view('create'))
exercisejournals.add_url_rule('/exercisejournals/<id>/', view_func=ShowExercisejournal.as_view('show'))
exercisejournals.add_url_rule('/exercisejournals/edit/<id>/', view_func=NewExercisejournal.as_view('edit'))