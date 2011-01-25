django-multiforloop provides an enhancement to django's builtin forloop
template tag, which makes it easier to iterate over multiple lists
simultaneously (acting similarly to Python's `zip`).

multiforloop allows this Python idiom to be used in django templates:

for x,y in zip(x_list, y_list):
	print x,y

Normally, to iterate over multiple lists simultaneously in django templates,
the lists must be zipped in the view and passed in as an extra context
variable. When this is the only extra processing needed in a view (eg. with
generic views), this can result in a fair bit of unneeded boilerplate code. 

##Usage

Rendering this template

    {% load multifor %}
    {% for x in x_list; y in y_list %}
      {{ x }}:{{ y }}
    {% endfor %}

with this context

    context = {
        "x_list": ('one', 1, 'carrot'),
        "y_list": ('two', 2, 'orange')
    }

will output

    one:two
    1:2
    carrot:orange

The multifor tag library also includes a `for_longest` tag that functions
similarly to izip_longest from Python's itertools library. Whereas the
normal for loop will truncate all inputs to the length of the shortest,
for_longest will iterate over all values of the longest, filling any shorter
inputs with the value in settings.TEMPLATE_STRING_IF_INVALID ('' by default).

Observe the difference:


Rendering this template

    {% load multifor %}
    {% for x in x_list; y in y_list %}
      {{ x }}:{{ y }}
    {% endfor %}

with this context

    context = {
        "x_list": ('one', 1, 'carrot'),
        "y_list": ('two', 2)
    }

will output

    one:two
    1:2

While rendering this template

    {% load multifor %}
    {% for_longest x in x_list; y in y_list %}
      {{ x }}:{{ y }}
    {% endfor %}

with the same context

    context = {
        "x_list": ('one', 1, 'carrot'),
        "y_list": ('two', 2)
    }

will output

    one:two
    1:2
    carrot:

## Installation

1. pip install django-multiforloop
2. Include 'multiforloop' in your settings.py's list of installed apps
3. Add `{% load multifor %}` to the top of any templates which use the multiforloop

