from django import template

register = template.Library()


@register.filter
def field_type(bound_field):
    return bound_field.field.widget.__class__.__name__


# CSS classes in Bootstrap forms
@register.filter
def input_class(bound_field):
    css_class = ''
    if bound_field.form.is_bound:
        if bound_field.errors:
            css_class = 'is-invalid'
        elif field_type(bound_field) != 'PasswordInput':
            css_class = 'is-valid'
    if field_type(bound_field) in {'FileInput', 'ClearableFileInput'}:
        return f'form-control-file {css_class}'
    else:
        return f'form-control {css_class}'
