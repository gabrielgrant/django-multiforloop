
from django.test import TestCase
from django.template import Context, Template

class TagTests(TestCase):
	def tag_test(self, template, context, output):
		t = Template('{% load multifor %}'+template)
		c = Context(context)
		self.assertEqual(t.render(c), output)
	def test_for_tag_multi(self):
		template = "{% for x in x_list; y in y_list %}{{ x }}:{{ y }}/{% endfor %}"
		context = {"x_list": ('one', 1, 'carrot'), "y_list": ('two', 2, 'orange')}
		output = u"one:two/1:2/carrot:orange/"
		self.tag_test(template, context, output)
		
	def test_for_tag_multi_unpack(self):
		self.tag_test("{% for x in x_list; y,z in yz_list %}{{ x }}:{{ y }}, {{ z }}/{% endfor %}", {"x_list": ('x1', 'x2', 'x3'), "yz_list": (('y1', 'z1'), ('y2', 'z2'), ('y3', 'z3'))}, u"x1:y1, z1/x2:y2, z2/x3:y3, z3/")
		
	def test_for_tag_multi_truncate(self):
		self.tag_test("{% for x in x_list; y in y_list %}{{ x }}:{{ y }}/{% endfor %}", {"x_list": ('one', 1, 'carrot'), "y_list":('two', 2)}, u"one:two/1:2/")
	
	def test_for_tag_multi_reversed(self):
		self.tag_test("{% for x in x_list reversed; y in y_list %}{{ x }}:{{ y }}/{% endfor %}", {"x_list": ('x1', 'x2', 'x3'), "y_list": ('y1', 'y2', 'y3')}, u"x3:y1/x2:y2/x1:y3/")

	def test_for_tag_multi_longest(self):
		template = "{% for_longest x in x_list; y in y_list %}{{ x }}:{{ y }}/{% endfor %}"
		context = {"x_list": ('one', 1, 'carrot', 'apple'), "y_list": ('two', 2, 'orange')}
		output = u"one:two/1:2/carrot:orange/apple:INVALID/"
		self.tag_test(template, context, output)

	def test_for_tag_multi_longest_empty(self):
		template = "{% for_longest x in x_list; y in y_list %}{{ x }}:{{ y }}/{% endfor %}"
		context = {"x_list": ('one', 1, 'carrot', 'apple')}
		output = u"one:INVALID/1:INVALID/carrot:INVALID/apple:INVALID/"
		self.tag_test(template, context, output)

	def test_for_tag_multi_longest_null(self):
		template = "{% for_longest x in x_list; y in y_list %}{{ x }}:{{ y }}/{% endfor %}"
		context = {"x_list": ('one', 1, 'carrot', 'apple'), "y_list": ()}
		output = u"one:INVALID/1:INVALID/carrot:INVALID/apple:INVALID/"
		self.tag_test(template, context, output)

