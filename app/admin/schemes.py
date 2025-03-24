from marshmallow import Schema, fields


class AdminSchema(Schema):
    id = fields.Int()
    email = fields.Str(required=True)
    password = fields.Str(required=False)


class ThemeSchema(Schema):
    id = fields.Int(required=False)
    title = fields.Str(required=True)


class QuestionSchema(Schema):
    id = fields.Int(required=False)
    title = fields.Str(required=True)
    theme_id = fields.Int(required=True)
    answers = fields.List(fields.Str(), required=True)


class AnswerSchema(Schema):
    id = fields.Int(required=False)
    text = fields.Str(required=True)
    question_id = fields.Int(required=True)


class ThemeListSchema(Schema):
    themes = fields.List(fields.Nested(ThemeSchema))


class ListQuestionSchema(Schema):
    questions = fields.List(fields.Nested(QuestionSchema))
