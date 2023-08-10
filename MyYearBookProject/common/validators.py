from django.core.exceptions import ValidationError


def validate_comment_text(value):
    inappropriate_words = ['bad', 'inappropriate', 'offensive']  # Replace with your list of inappropriate words
    for word in inappropriate_words:
        if word in value:
            raise ValidationError
