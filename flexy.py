from __future__ import unicode_literals, absolute_import

import unittest

from linebot.models import (
    TemplateSendMessage,
    CarouselTemplate,
    CarouselColumn,
    ImageCarouselTemplate,
    ImageCarouselColumn,
    ConfirmTemplate,
    ButtonsTemplate,
    PostbackAction,
    URIAction,
    MessageAction,
)

from tests.models.serialize_test_case import SerializeTestCase


class TestTemplate(SerializeTestCase):
    def test_template(self):
        arg = {
            'type': 'template',
            'alt_text': 'This is a buttons template',
            'template':
                ButtonsTemplate(
                    thumbnail_image_url='https://img.tek.id/img/content/2019/07/04/17857/line-resmi-hadirkan-gim-hello-bt21-vZhHl6aAVg.jpg',
                    image_aspect_ratio='rectangle',
                    image_size='cover',
                    image_background_color='#FFFFFF',
                    title='Menu',
                    text='Please select',
                    default_action=URIAction(label='View detail',
                                             uri='https://img.tek.id/img/content/2019/07/04/17857/line-resmi-hadirkan-gim-hello-bt21-vZhHl6aAVg.jpg'),
                    actions=[
                        PostbackAction(label='Buy', data='action=buy&itemid=155'),
                        URIAction(label='View detail', uri='https://img.tek.id/img/content/2019/07/04/17857/line-resmi-hadirkan-gim-hello-bt21-vZhHl6aAVg.jpg'),
                    ]
                )
        }
        self.assertEqual(
            self.serialize_as_dict(arg, type=self.TEMPLATE),
            TemplateSendMessage(**arg).as_json_dict()
        )

    def test_button_template(self):
        arg = {
            'type': 'buttons',
            'thumbnail_image_url': 'https://img.tek.id/img/content/2019/07/04/17857/line-resmi-hadirkan-gim-hello-bt21-vZhHl6aAVg.jpg',
            'image_aspect_ratio': 'rectangle',
            'image_size': 'cover',
            'image_background_color': '#FFFFFF',
            'title': 'Menu',
            'text': 'Please select',
            'default_action': URIAction(label='View detail',
                                        uri='https://img.tek.id/img/content/2019/07/04/17857/line-resmi-hadirkan-gim-hello-bt21-vZhHl6aAVg.jpg'),
            'actions': [
                PostbackAction(label='Buy', data='action=buy&itemid=155'),
                URIAction(label='View detail', uri='https://img.tek.id/img/content/2019/07/04/17857/line-resmi-hadirkan-gim-hello-bt21-vZhHl6aAVg.jpg'),
            ]
        }
        self.assertEqual(
            self.serialize_as_dict(arg, type=self.BUTTONS),
            ButtonsTemplate(**arg).as_json_dict()
        )

    def test_confirm_template(self):
        arg = {
            'type': 'confirm',
            'text': 'Are you sure?',
            'actions': [
                MessageAction(label='Yes', text='yes...'),
                MessageAction(label='No', text='no...'),
            ]
        }
        self.assertEqual(
            self.serialize_as_dict(arg, type=self.CONFIRM),
            ConfirmTemplate(**arg).as_json_dict()
        )

    def test_carousel_template(self):
        arg = {
            'image_aspect_ratio': 'rectangle',
            'image_size': 'cover',
            'columns': [
                CarouselColumn(
                    thumbnail_image_url='https://img.tek.id/img/content/2019/07/04/17857/line-resmi-hadirkan-gim-hello-bt21-vZhHl6aAVg.jpg',
                    image_background_color='#FFFFFF',
                    title='this is menu',
                    text='description',
                    default_action=URIAction(label='View detail',
                                             uri='https://img.tek.id/img/content/2019/07/04/17857/line-resmi-hadirkan-gim-hello-bt21-vZhHl6aAVg.jpg'),
                    actions=[
                        PostbackAction(label='Buy', data='action=buy&itemid=155'),
                        URIAction(label='View detail', uri='https://img.tek.id/img/content/2019/07/04/17857/line-resmi-hadirkan-gim-hello-bt21-vZhHl6aAVg.jpg'),
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://img.tek.id/img/content/2019/07/04/17857/line-resmi-hadirkan-gim-hello-bt21-vZhHl6aAVg.jpg',
                    image_background_color='#000000',
                    title='this is menu',
                    text='description',
                    default_action=URIAction(label='View detail',
                                             uri='https://img.tek.id/img/content/2019/07/04/17857/line-resmi-hadirkan-gim-hello-bt21-vZhHl6aAVg.jpg'),
                    actions=[
                        PostbackAction(label='Buy', data='action=buy&itemid=555'),
                        URIAction(label='View detail', uri='https://img.tek.id/img/content/2019/07/04/17857/line-resmi-hadirkan-gim-hello-bt21-vZhHl6aAVg.jpg'),
                    ]
                )
            ]
        }
        self.assertEqual(
            self.serialize_as_dict(arg, type=self.CAROUSEL),
            CarouselTemplate(**arg).as_json_dict()
        )

    def test_carousel_column(self):
        arg = {
            'thumbnail_image_url': 'https://img.tek.id/img/content/2019/07/04/17857/line-resmi-hadirkan-gim-hello-bt21-vZhHl6aAVg.jpg',
            'image_background_color': '#FFFFFF',
            'title': 'this is menu',
            'text': 'description',
            'default_action': URIAction(label='View detail',
                                        uri='https://img.tek.id/img/content/2019/07/04/17857/line-resmi-hadirkan-gim-hello-bt21-vZhHl6aAVg.jpg'),
            'actions': [
                PostbackAction(label='Buy', data='action=buy&itemid=155'),
                URIAction(label='View detail', uri='https://img.tek.id/img/content/2019/07/04/17857/line-resmi-hadirkan-gim-hello-bt21-vZhHl6aAVg.jpg'),
            ]
        }
        self.assertEqual(
            self.serialize_as_dict(arg),
            CarouselColumn(**arg).as_json_dict()
        )

    def test_image_carousel_template(self):
        arg = {
            'columns': [
                ImageCarouselColumn(
                    image_url='https://img.tek.id/img/content/2019/07/04/17857/line-resmi-hadirkan-gim-hello-bt21-vZhHl6aAVg.jpg',
                    action=PostbackAction(label='Buy', data='action=buy&itemid=555')
                ),
                ImageCarouselColumn(
                    image_url='https://img.tek.id/img/content/2019/07/04/17857/line-resmi-hadirkan-gim-hello-bt21-vZhHl6aAVg.jpg',
                    action=MessageAction(label='Yes', text='yes')
                ),
            ]
        }
        self.assertEqual(
            self.serialize_as_dict(arg, type=self.IMAGE_CAROUSEL),
            ImageCarouselTemplate(**arg).as_json_dict()
        )

    def test_image_carousel_column(self):
        arg = {
            'image_url': 'https://img.tek.id/img/content/2019/07/04/17857/line-resmi-hadirkan-gim-hello-bt21-vZhHl6aAVg.jpg',
            'action': PostbackAction(label='Buy', data='action=buy&itemid=555')
        }
        self.assertEqual(
            self.serialize_as_dict(arg),
            ImageCarouselColumn(**arg).as_json_dict()
        )


if __name__ == '__main__':
    unittest.main()
