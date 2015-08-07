from flask import Blueprint, request, redirect, render_template, url_for
from flask.views import MethodView
from flask.ext.mongoengine.wtf import model_form
from weighttracker.models.measurement import Measurement
import parsedatetime
from datetime import datetime
from time import mktime

measurements = Blueprint('measurements', __name__, template_folder='templates')


class ListMeasurements(MethodView):

  def get(self, page=1):
    measurements = Measurement.objects.order_by('-measurement_time').paginate(page, per_page=10)
    return render_template('measurements/list.html', measurements=measurements)


class ShowMeasurement(MethodView):

  def get(self, id):
    measurement = Measurement.objects.get_or_404(id=id )
    return render_template('measurements/show.html', measurement=measurement)


class EditMeasurement(MethodView):

  def get(self, id):
    measurement = Measurement.objects.get_or_404(id=id )
    header_text = "Edit This Measurement"
    return render_template('measurements/edit.html', measurement=measurement, header_text=header_text)


class NewMeasurement(MethodView):

  def get_context(self, id=None):
    form_cls = model_form(Measurement, exclude=('created_at', 'updated_at'))

    if id:
      measurement = Measurement.objects.get_or_404(id=id)
      header_text = "Edit This Measurement"
      if request.method == 'POST':
        form = form_cls(request.form, initial=measurement._data)
      else:
        form = form_cls(obj=measurement)
    else:
      measurement = Measurement()
      header_text = "Add a New Measurement"
      form = form_cls(request.form)

    context = {
            "measurement": measurement,
            "form": form,
            "header_text": header_text,
            "create": id is None
    }

    return context


  def get(self, id=None):
    context = self.get_context(id)
    return render_template('measurements/new.html', **context)

  def post(self, id=None):
    context = self.get_context(id)
    form = context.get('form')

    if form.validate():
      measurement = context.get('measurement')
      form.populate_obj(measurement)

      # Add the measurement_time value, or update it
      cal = parsedatetime.Calendar()
      time_struct, parse_status = cal.parse(measurement['date'])
      measurement['measurement_time'] = datetime.fromtimestamp(mktime(time_struct))
      measurement['updated_at'] = datetime.now()

      measurement.save()

      return redirect(url_for('measurements.list'))
    return render_template('measurements/new.html', **context)



# Register the urls
measurements.add_url_rule('/measurements/', view_func=ListMeasurements.as_view('list'))
measurements.add_url_rule('/measurements/<int:page>/', view_func=ListMeasurements.as_view('listpage'))
measurements.add_url_rule('/measurements/new/', view_func=NewMeasurement.as_view('new'))
measurements.add_url_rule('/measurements/create/', defaults={'id': None}, view_func=NewMeasurement.as_view('create'))
measurements.add_url_rule('/measurements/<id>/', view_func=ShowMeasurement.as_view('show'))
measurements.add_url_rule('/measurements/edit/<id>/', view_func=NewMeasurement.as_view('edit'))