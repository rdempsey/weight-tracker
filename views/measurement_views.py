from flask import Blueprint, request, redirect, render_template, url_for
from flask.views import MethodView
from flask.ext.mongoengine.wtf import model_form
from weighttracker.models.measurement import Measurement

measurements = Blueprint('measurements', __name__, template_folder='templates')


class ListMeasurements(MethodView):

  def get(self):
    measurements = Measurement.objects.all()
    return render_template('measurements/list.html', measurements=measurements)



class ShowMeasurement(MethodView):

  def get(self, date):
    measurement = Measurement.objects.get_or_404(date=date )
    return render_template('measurements/show.html', measurement=measurement)


class EditMeasurement(MethodView):

  def get(self, date):
    measurement = Measurement.objects.get_or_404(date=date )
    return render_template('measurements/edit.html', measurement=measurement)


class NewMeasurement(MethodView):

  def get_context(self, date=None):
    form_cls = model_form(Measurement, exclude=('created_at', 'updated_at'))

    if date:
      measurement = Measurement.objects.get_or_404(date=date)
      if request.method == 'POST':
        form = form_cls(request.form, inital=measurement._data)
      else:
        form = form_cls(obj=measurement)
    else:
      measurement = Measurement()
      form = form_cls(request.form)

    context = {
            "measurement": measurement,
            "form": form,
            "create": date is None
    }

    return context


  def get(self, date=None):
    context = self.get_context(date)
    return render_template('measurements/new.html', **context)

  def post(self, date=None):
    context = self.get_context(date)
    form = context.get('form')

    if form.validate():
      measurement = context.get('measurement')
      form.populate_obj(measurement)
      measurement.save()

      return redirect(url_for('measurements.list'))
    return render_template('measurements/new.html', **context)



# Register the urls
measurements.add_url_rule('/measurements/', view_func=ListMeasurements.as_view('list'))
measurements.add_url_rule('/measurements/new/', view_func=NewMeasurement.as_view('new'))
measurements.add_url_rule('/measurements/create/', defaults={'date': None}, view_func=NewMeasurement.as_view('create'))
measurements.add_url_rule('/measurements/<date>/', view_func=ShowMeasurement.as_view('show'))
measurements.add_url_rule('/measurements/edit/<date>/', view_func=EditMeasurement.as_view('edit'))