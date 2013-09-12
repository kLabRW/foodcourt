# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Restaurant_detail'
        db.create_table(u'restaurant_detail_restaurant_detail', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='restaurant_detail_creations', to=orm['auth.User'])),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='restaurant_detail_modifications', to=orm['auth.User'])),
            ('modified_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('mobile', self.gf('phonenumber_field.modelfields.PhoneNumberField')(max_length=18)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=74)),
            ('restaurant_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('logo', self.gf('django.db.models.fields.files.ImageField')(max_length=500, null=True, blank=True)),
            ('cusine', self.gf('django.db.models.fields.TextField')()),
            ('service_type', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('service_fee', self.gf('django.db.models.fields.IntegerField')(max_length=5, null=True, blank=True)),
            ('service_days', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('service_hours_start', self.gf('django.db.models.fields.TimeField')()),
            ('service_hours_end', self.gf('django.db.models.fields.TimeField')()),
            ('minimum_order_amount', self.gf('django.db.models.fields.IntegerField')(max_length=5, null=True, blank=True)),
            ('delivery_territory', self.gf('django.db.models.fields.TextField')(max_length=500, null=True, blank=True)),
            ('closed', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'restaurant_detail', ['Restaurant_detail'])

        # Adding model 'Restaurant'
        db.create_table(u'restaurant_detail_restaurant', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='restaurant_creations', to=orm['auth.User'])),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='restaurant_modifications', to=orm['auth.User'])),
            ('modified_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['auth.User'])),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('mobile', self.gf('phonenumber_field.modelfields.PhoneNumberField')(max_length=18)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=74)),
            ('restaurant_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('logo', self.gf('django.db.models.fields.files.ImageField')(max_length=600, null=True, blank=True)),
            ('cusine', self.gf('django.db.models.fields.TextField')()),
            ('service_type', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('service_fee', self.gf('django.db.models.fields.IntegerField')(max_length=5, null=True, blank=True)),
            ('service_days', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('service_hours_start', self.gf('django.db.models.fields.TimeField')()),
            ('service_hours_end', self.gf('django.db.models.fields.TimeField')()),
            ('minimum_order_amount', self.gf('django.db.models.fields.IntegerField')(default='1', max_length=5)),
            ('delivery_territory', self.gf('django.db.models.fields.TextField')(max_length=500, null=True, blank=True)),
            ('closed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('token', self.gf('django.db.models.fields.CharField')(unique=True, max_length=32)),
            ('restaurant_detail', self.gf('django.db.models.fields.related.ForeignKey')(default='1', to=orm['restaurant_detail.Restaurant_detail'])),
            ('rating_votes', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, blank=True)),
            ('rating_score', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
        ))
        db.send_create_signal(u'restaurant_detail', ['Restaurant'])

        # Adding model 'Item'
        db.create_table('items', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='item_creations', to=orm['auth.User'])),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='item_modifications', to=orm['auth.User'])),
            ('modified_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('display_order', self.gf('django.db.models.fields.IntegerField')(max_length=3)),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['restaurant_detail.Restaurant'])),
        ))
        db.send_create_signal(u'restaurant_detail', ['Item'])

        # Adding M2M table for field optionalitems on 'Item'
        m2m_table_name = db.shorten_name('items_optionalitems')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('item', models.ForeignKey(orm[u'restaurant_detail.item'], null=False)),
            ('optionalitemcategory', models.ForeignKey(orm[u'optionalitems.optionalitemcategory'], null=False))
        ))
        db.create_unique(m2m_table_name, ['item_id', 'optionalitemcategory_id'])

        # Adding M2M table for field Options on 'Item'
        m2m_table_name = db.shorten_name('items_Options')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('item', models.ForeignKey(orm[u'restaurant_detail.item'], null=False)),
            ('optional_item', models.ForeignKey(orm[u'optionalitems.optional_item'], null=False))
        ))
        db.create_unique(m2m_table_name, ['item_id', 'optional_item_id'])

        # Adding model 'Category'
        db.create_table('categories', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='category_creations', to=orm['auth.User'])),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='category_modifications', to=orm['auth.User'])),
            ('modified_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('display_order', self.gf('django.db.models.fields.IntegerField')(max_length=3)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(related_name='category', to=orm['restaurant_detail.Restaurant'])),
        ))
        db.send_create_signal(u'restaurant_detail', ['Category'])

        # Adding M2M table for field item on 'Category'
        m2m_table_name = db.shorten_name('categories_item')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('category', models.ForeignKey(orm[u'restaurant_detail.category'], null=False)),
            ('item', models.ForeignKey(orm[u'restaurant_detail.item'], null=False))
        ))
        db.create_unique(m2m_table_name, ['category_id', 'item_id'])


    def backwards(self, orm):
        # Deleting model 'Restaurant_detail'
        db.delete_table(u'restaurant_detail_restaurant_detail')

        # Deleting model 'Restaurant'
        db.delete_table(u'restaurant_detail_restaurant')

        # Deleting model 'Item'
        db.delete_table('items')

        # Removing M2M table for field optionalitems on 'Item'
        db.delete_table(db.shorten_name('items_optionalitems'))

        # Removing M2M table for field Options on 'Item'
        db.delete_table(db.shorten_name('items_Options'))

        # Deleting model 'Category'
        db.delete_table('categories')

        # Removing M2M table for field item on 'Category'
        db.delete_table(db.shorten_name('categories_item'))


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
        u'restaurant_detail.category': {
            'Meta': {'object_name': 'Category', 'db_table': "'categories'"},
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'category_creations'", 'to': u"orm['auth.User']"}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'display_order': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'item': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['restaurant_detail.Item']", 'symmetrical': 'False'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'category_modifications'", 'to': u"orm['auth.User']"}),
            'modified_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'category'", 'to': u"orm['restaurant_detail.Restaurant']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '64'})
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
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'})
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

    complete_apps = ['restaurant_detail']