#!/usr/bin/env python
# encoding: utf-8
"""
codegen.py
Created by Robert Dempsey on 08/13/2015

Given a model name and a dict with the field names and types it creates a
model, view and templates in the appropriate directories
Minimal customization is then needed
"""

import os
from jinja2 import Environment, FileSystemLoader

PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    loader=FileSystemLoader(os.path.join(PATH, 'code_templates')),
    trim_blocks=False)


def render_template(template_filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)


def create_class_file():
    # Define the name of the model and list the fields along with their type.
    # NOTE: write the model name in the singular, so "goal" not "goals"
    # NOTE: created_at, updated_at and deleted_at are included in the model
    model_name = 'goal'
    fields = {
        'current_weight': 'decimal',
        'current_bodyfat': 'decimal',
        'training_status': 'string',
        'weekly_hours_of_training': 'decimal',
        'intensity_of_effort': 'decimal',
        'goal': 'string',
        'daily_target_calories': 'decimal',
        'daily_target_protein': 'decimal',
        'daily_target_carbs': 'decimal',
        'daily_target_fat': 'decimal'
    }

    context = {
        'model_name': model_name,
        'fields': fields
    }

    # Create the model file
    model_file = "../models/{}.py".format(model_name)
    with open(model_file, 'w') as f:
        html = render_template('model.html', context)
        f.write(html)

    # Create the view file
    view_file = "../views/{}_views.py".format(model_name)
    with open(view_file, 'w') as f:
        html = render_template('view.html', context)
        f.write(html)

    # Create the directory for the template files
    template_dir = "../templates/{}s".format(model_name)
    if not os.path.exists(template_dir):
        os.mkdir(template_dir)

    # List template
    list_template = template_dir + "/" + "list.html"
    with open(list_template, 'w') as f:
        html = render_template('list.html', context)
        f.write(html)

    # New template
    new_template = template_dir + "/" + "new.html"
    with open(new_template, 'w') as f:
        html = render_template('new.html', context)
        f.write(html)

    # Show template
    show_template = template_dir + "/" + "show.html"
    with open(show_template, 'w+') as f:
        html = render_template('show.html', context)
        f.write(html)


def main():
    create_class_file()

if __name__ == "__main__":
    main()
