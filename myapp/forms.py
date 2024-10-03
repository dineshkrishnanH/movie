from django import forms

class MovieForm(forms.Form):

    title=forms.CharField()

    options=(
        ("Action","action"),
        ("Fiction","Fiction"),
        ("Drama","Drama"),
        ("comdey","comdey"),
    )

    genre=forms.CharField()

    language=forms.CharField()

    year=forms.CharField()

    run_time=forms.IntegerField()

    director=forms.CharField()

def clean(self):

    clean_data=super().clean()

    year=clean_data.get("year")

    if (int(year)<1990):

        error_message="enter msg 1990"

        self.add_error("year",error_message)






