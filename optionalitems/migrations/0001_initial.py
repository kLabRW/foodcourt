# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'OptionalItem'
        db.create_table(u'optionalitems_optionalitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='optionalitem_creations', to=orm['auth.User'])),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='optionalitem_modifications', to=orm['auth.User'])),
            ('modified_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('price', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=9, decimal_places=2, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['restaurant_detail.Restaurant'])),
        ))
        db.send_create_signal(u'optionalitems', ['OptionalItem'])

        # Adding model 'OptionalItemCategory'
        db.create_table(u'optionalitems_optionalitemcategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='optionalitemcategory_creations', to=orm['auth.User'])),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='optionalitemcategory_modifications', to=orm['auth.User'])),
            ('modified_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('display_order', self.gf('django.db.models.fields.IntegerField')(max_length=3)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['restaurant_detail.Restaurant'])),
        ))
        db.send_create_signal(u'optionalitems', ['OptionalItemCategory'])

        # Adding M2M table for field optional_items on 'OptionalItemCategory'
        m2m_table_name = db.shorten_name(u'optionalitems_optionalitemcategory_optional_items')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('optionalitemcategory', models.ForeignKey(orm[u'optionalitems.optionalitemcategory'], null=False)),
            ('optionalitem', models.ForeignKey(orm[u'optionalitems.optionalitem'], null=False))
        ))
        db.create_unique(m2m_table_name, ['optionalitemcategory_id', 'optionalitem_id'])

        # Adding model 'ToppingsAndExtra'
        db.create_table(u'optionalitems_toppingsandextra', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='toppingsandextra_creations', to=orm['auth.User'])),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='toppingsandextra_modifications', to=orm['auth.User'])),
            ('modified_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('price', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=9, decimal_places=2, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=140, null=True, blank=True)),
        ))
        db.send_create_signal(u'optionalitems', ['ToppingsAndExtra'])

        # Adding model 'ToppingsAndExtrasCategory'
        db.create_table(u'optionalitems_toppingsandextrascategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='toppingsandextrascategory_creations', to=orm['auth.User'])),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='toppingsandextrascategory_modifications', to=orm['auth.User'])),
            ('modified_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('display_order', self.gf('django.db.models.fields.IntegerField')(max_length=3)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['restaurant_detail.Restaurant'])),
        ))
        db.send_create_signal(u'optionalitems', ['ToppingsAndExtrasCategory'])

        # Adding M2M table for field toppings_and_extras on 'ToppingsAndExtrasCategory'
        m2m_table_name = db.shorten_name(u'optionalitems_toppingsandextrascategory_toppings_and_extras')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('toppingsandextrascategory', models.ForeignKey(orm[u'optionalitems.toppingsandextrascategory'], null=False)),
            ('toppingsandextra', models.ForeignKey(orm[u'optionalitems.toppingsandextra'], null=False))
        ))
        db.create_unique(m2m_table_name, ['toppingsandextrascategory_id', 'toppingsandextra_id'])


    def backwards(self, orm):
        # Deleting model 'OptionalItem'
        db.delete_table(u'optionalitems_optionalitem')

        # Deleting model 'OptionalItemCategory'
        db.delete_table(u'optionalitems_optionalitemcategory')

        # Removing M2M table for field optional_items on 'OptionalItemCategory'
        db.delete_table(db.shorten_name(u'optionalitems_optionalitemcategory_optional_items'))

        # Deleting model 'ToppingsAndExtra'
        db.delete_table(u'optionalitems_toppingsandextra')

        # Deleting model 'ToppingsAndExtrasCategory'
        db.delete_table(u'optionalitems_toppingsandextrascategory')

        # Removing M2M table for field toppings_and_extras on 'ToppingsAndExtrasCategory'
        db.delete_table(db.shorten_name(u'optionalitems_toppingsandextrascategory_toppings_and_extras'))


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
        u'optionalitems.optionalitem': {
            'Meta': {'object_name': 'OptionalItem'},
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'optionalitem_creations'", 'to': u"orm['auth.User']"}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'optionalitem_modifications'", 'to': u"orm['auth.User']"}),
            'modified_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
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
            'optional_items': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['optionalitems.OptionalItem']", 'symmetrical': 'False'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['restaurant_detail.Restaurant']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '140'})
        },
        u'optionalitems.toppingsandextra': {
            'Meta': {'object_name': 'ToppingsAndExtra'},
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'toppingsandextra_creations'", 'to': u"orm['auth.User']"}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'toppingsandextra_modifications'", 'to': u"orm['auth.User']"}),
            'modified_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'price': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '9', 'decimal_places': '2', 'blank': 'True'})
        },
        u'optionalitems.toppingsandextrascategory': {
            'Meta': {'object_name': 'ToppingsAndExtrasCategory'},
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'toppingsandextrascategory_creations'", 'to': u"orm['auth.User']"}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'display_order': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'toppingsandextrascategory_modifications'", 'to': u"orm['auth.User']"}),
            'modified_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['restaurant_detail.Restaurant']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'toppings_and_extras': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['optionalitems.ToppingsAndExtra']", 'symmetrical': 'False'})
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
            'restaurant_detail': ('django.db.models.fields.related.ForeignKey', [], {'default': "'1'", 'to': u"orm['restaurant_detail.RestaurantDetail']"}),
            'restaurant_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'service_days': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'service_fee': ('django.db.models.fields.IntegerField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'service_hours_end': ('django.db.models.fields.TimeField', [], {}),
            'service_hours_start': ('django.db.models.fields.TimeField', [], {}),
            'service_type': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'token': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['auth.User']"})
        },
        u'restaurant_detail.restaurantdetail': {
            'Meta': {'object_name': 'RestaurantDetail'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'closed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'restaurantdetail_creations'", 'to': u"orm['auth.User']"}),
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
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'restaurantdetail_modifications'", 'to': u"orm['auth.User']"}),
            'modified_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'restaurant_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'service_days': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'service_fee': ('django.db.models.fields.IntegerField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'service_hours_end': ('django.db.models.fields.TimeField', [], {}),
            'service_hours_start': ('django.db.models.fields.TimeField', [], {}),
            'service_type': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        }
    }

    complete_apps = ['optionalitems']