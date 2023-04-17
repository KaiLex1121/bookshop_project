from django import forms


class FeedBackForm(forms.Form):

    first_name = forms.CharField(min_length=3, max_length=30, error_messages={
        "min_length": 'Минимальное количество символов - 3',
        "max_length": 'Максимальное количество символов - 30',
        "required": 'Поле должно быть заполнено'
    })
    last_name = forms.CharField()
    description = forms.CharField(widget=(forms.Textarea()))
    rating = forms.IntegerField(max_value=5)
