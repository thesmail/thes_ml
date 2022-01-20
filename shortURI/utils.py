from django.conf import settings

from random import choice

from string import ascii_letters

SIZE = getattr(settings, "MAXIMUM_URL_CHARS", 3)

AVAIABLE_CHARS = ascii_letters


def create_random_code(chars=AVAIABLE_CHARS):
    return "".join(
        [choice(chars) for _ in range(SIZE)]
    )

def create_shortened_url(model_instance):
    random_code = create_random_code()
    # Gets the model class

    model_class = model_instance.__class__

    if model_class.objects.filter(short_url=random_code).exists():
        # Run the function again
        return create_shortened_url(model_instance)

    return random_code