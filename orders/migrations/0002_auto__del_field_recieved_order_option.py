# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Recieved_Order.option'
        db.delete_column(u'orders_recieved_order', 'option_id')


    def backwards(self, orm):
        # Adding field 'Recieved_Order.option'
        db.add_column(u'orders_recieved_order', 'option',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['optionalitems.Optional_Item']),
                      keep_default=False)


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'optionalitems.optional_item': {
            'Meta': {'object_name': 'Optional_Item'},
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'optional_item_creations'", 'to': u"orm['auth.User']"}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'optional_item_modifications'", 'to': u"orm['auth.User']"}),
            'modified_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['restaurant_detail.Restaurant']"}),
            'price': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '9', 'decimal_places': '2', 'blank': 'True'})
        },
        u'optionalitems.optionalitemcategory': {
            'Meta': {'object_name': 'OptionalItemCategory'},
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'optionalitemcategory_creations'", 'to': u"orm['auth.User']"}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'display_order': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'optionalitemcategory_modifications'", 'to': u"orm['auth.User']"}),
            'modified_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'optional_items': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['optionalitems.Optional_Item']", 'symmetrical': 'False'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['restaurant_detail.Restaurant']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'orders.order': {
            'Meta': {'object_name': 'Order'},
            'additional_information': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'address': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'order_creations'", 'to': u"orm['auth.User']"}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'mobile': ('phonenumber_field.modelfields.PhoneNumberField', [], {'max_length': '20'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'order_modifications'", 'to': u"orm['auth.User']"}),
            'modified_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'restaurant': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['restaurant_detail.Restaurant']", 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        u'orders.orderitem': {
            'Meta': {'object_name': 'OrderItem', 'db_table': "'order_items'"},
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'orderitem_creations'", 'to': u"orm['auth.User']"}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['restaurant_detail.Item']"}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'orderitem_modifications'", 'to': u"orm['auth.User']"}),
            'modified_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'option': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['optionalitems.Optional_Item']"}),
            'quantity': ('django.db.models.fields.IntegerField', [], {}),
            'shopping_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'})
        },
        u'orders.recieved_order': {
            'Meta': {'object_name': 'Recieved_Order'},
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'recieved_order_creations'", 'to': u"orm['auth.User']"}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['restaurant_detail.Item']"}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'recieved_order_modifications'", 'to': u"orm['auth.User']"}),
            'modified_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['orders.Order']"}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'restaurant_detail.item': {
            'Meta': {'object_name': 'Item', 'db_table': "'items'"},
            'Options': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['optionalitems.Optional_Item']", 'null': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'item_creations'", 'to': u"orm['auth.User']"}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'display_order': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'item_modifications'", 'to': u"orm['auth.User']"}),
            'modified_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'optionalitems': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['optionalitems.OptionalItemCategory']", 'null': 'True', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['restaurant_detail.Restaurant']"}),
            'price': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '9', 'decimal_places': '2', 'blank': 'True'})
        },
        u'restaurant_detail.restaurant': {
            'Meta': {'object_name': 'Restaurant'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'closed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'restaurant_creations'", 'to': u"orm['auth.User']"}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'cusine': ('django.db.models.fields.TextField', [], {}),
            'delivery_territory': ('django.db.models.fields.TextField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '74'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '600', 'null': 'True', 'blank': 'True'}),
            'minimum_order_amount': ('django.db.models.fields.IntegerField', [], {'default': "'1'", 'max_length': '5'}),
            'mobile': ('phonenumber_field.modelfields.PhoneNumberField', [], {'max_length': '18'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'restaurant_modifications'", 'to': u"orm['auth.User']"}),
            'modified_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'rating_score': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'rating_votes': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'}),
            'restaurant_detail': ('django.db.models.fields.related.ForeignKey', [], {'default': "'1'", 'to': u"orm['restaurant_detail.Restaurant_detail']"}),
            'restaurant_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'service_days': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'service_fee': ('django.db.models.fields.IntegerField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'service_hours_end': ('django.db.models.fields.TimeField', [], {}),
            'service_hours_start': ('django.db.models.fields.TimeField', [], {}),
            'service_type': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'token': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['auth.User']"})
        },
        u'restaurant_detail.restaurant_detail': {
            'Meta': {'object_name': 'Restaurant_detail'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'closed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'restaurant_detail_creations'", 'to': u"orm['auth.User']"}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'cusine': ('django.db.models.fields.TextField', [], {}),
            'delivery_territory': ('django.db.models.fields.TextField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '74'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'minimum_order_amount': ('django.db.models.fields.IntegerField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'mobile': ('phonenumber_field.modelfields.PhoneNumberField', [], {'max_length': '18'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'restaurant_detail_modifications'", 'to': u"orm['auth.User']"}),
            'modified_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'restaurant_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'service_days': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'service_fee': ('django.db.models.fields.IntegerField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'service_hours_end': ('django.db.models.fields.TimeField', [], {}),
            'service_hours_start': ('django.db.models.fields.TimeField', [], {}),
            'service_type': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        }
    }

    complete_apps = ['orders']