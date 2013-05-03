# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Restaurant_detail'
        db.create_table('restaurant_detail_restaurant_detail', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
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
            ('service_days', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('service_hours_start', self.gf('django.db.models.fields.TimeField')()),
            ('service_hours_end', self.gf('django.db.models.fields.TimeField')()),
            ('minimum_order_amount', self.gf('django.db.models.fields.IntegerField')(max_length=5)),
            ('delivery_territory', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('restaurant_detail', ['Restaurant_detail'])

        # Adding model 'Restaurant'
        db.create_table('restaurant_detail_restaurant', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='restaurant_creations', to=orm['auth.User'])),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='restaurant_modifications', to=orm['auth.User'])),
            ('modified_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['auth.User'])),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('mobile', self.gf('phonenumber_field.modelfields.PhoneNumberField')(default='+25078######', max_length=18)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=74)),
            ('restaurant_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('logo', self.gf('django.db.models.fields.files.ImageField')(max_length=500, null=True, blank=True)),
            ('cusine', self.gf('django.db.models.fields.TextField')()),
            ('service_type', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('service_fee', self.gf('django.db.models.fields.IntegerField')(max_length=5, null=True, blank=True)),
            ('service_days', self.gf('django.db.models.fields.CharField')(max_length=5, null=True, blank=True)),
            ('service_hours_start', self.gf('django.db.models.fields.TimeField')()),
            ('service_hours_end', self.gf('django.db.models.fields.TimeField')()),
            ('minimum_order_amount', self.gf('django.db.models.fields.IntegerField')(default='1', max_length=5)),
            ('delivery_territory', self.gf('django.db.models.fields.TextField')()),
            ('token', self.gf('django.db.models.fields.CharField')(unique=True, max_length=32)),
            ('restaurant_detail', self.gf('django.db.models.fields.related.ForeignKey')(default='1', to=orm['restaurant_detail.Restaurant_detail'])),
            ('rating_votes', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, blank=True)),
            ('rating_score', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
        ))
        db.send_create_signal('restaurant_detail', ['Restaurant'])

        # Adding model 'Item'
        db.create_table('items', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
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
        db.send_create_signal('restaurant_detail', ['Item'])

        # Adding model 'Category'
        db.create_table('categories', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
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
        db.send_create_signal('restaurant_detail', ['Category'])

        # Adding M2M table for field item on 'Category'
        db.create_table('categories_item', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('category', models.ForeignKey(orm['restaurant_detail.category'], null=False)),
            ('item', models.ForeignKey(orm['restaurant_detail.item'], null=False))
        ))
        db.create_unique('categories_item', ['category_id', 'item_id'])


    def backwards(self, orm):
        # Deleting model 'Restaurant_detail'
        db.delete_table('restaurant_detail_restaurant_detail')

        # Deleting model 'Restaurant'
        db.delete_table('restaurant_detail_restaurant')

        # Deleting model 'Item'
        db.delete_table('items')

        # Deleting model 'Category'
        db.delete_table('categories')

        # Removing M2M table for field item on 'Category'
        db.delete_table('categories_item')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'restaurant_detail.category': {
            'Meta': {'object_name': 'Category', 'db_table': "'categories'"},
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'category_creations'", 'to': "orm['auth.User']"}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'display_order': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'item': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['restaurant_detail.Item']", 'symmetrical': 'False'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'category_modifications'", 'to': "orm['auth.User']"}),
            'modified_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'category'", 'to': "orm['restaurant_detail.Restaurant']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        'restaurant_detail.item': {
            'Meta': {'object_name': 'Item', 'db_table': "'items'"},
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'item_creations'", 'to': "orm['auth.User']"}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'display_order': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'item_modifications'", 'to': "orm['auth.User']"}),
            'modified_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['restaurant_detail.Restaurant']"}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'})
        },
        'restaurant_detail.restaurant': {
            'Meta': {'object_name': 'Restaurant'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'restaurant_creations'", 'to': "orm['auth.User']"}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'cusine': ('django.db.models.fields.TextField', [], {}),
            'delivery_territory': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '74'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'minimum_order_amount': ('django.db.models.fields.IntegerField', [], {'default': "'1'", 'max_length': '5'}),
            'mobile': ('phonenumber_field.modelfields.PhoneNumberField', [], {'default': "'+25078######'", 'max_length': '18'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'restaurant_modifications'", 'to': "orm['auth.User']"}),
            'modified_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'rating_score': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'rating_votes': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'}),
            'restaurant_detail': ('django.db.models.fields.related.ForeignKey', [], {'default': "'1'", 'to': "orm['restaurant_detail.Restaurant_detail']"}),
            'restaurant_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'service_days': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'service_fee': ('django.db.models.fields.IntegerField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'service_hours_end': ('django.db.models.fields.TimeField', [], {}),
            'service_hours_start': ('django.db.models.fields.TimeField', [], {}),
            'service_type': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'token': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': "orm['auth.User']"})
        },
        'restaurant_detail.restaurant_detail': {
            'Meta': {'object_name': 'Restaurant_detail'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'restaurant_detail_creations'", 'to': "orm['auth.User']"}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'cusine': ('django.db.models.fields.TextField', [], {}),
            'delivery_territory': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '74'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'minimum_order_amount': ('django.db.models.fields.IntegerField', [], {'max_length': '5'}),
            'mobile': ('phonenumber_field.modelfields.PhoneNumberField', [], {'max_length': '18'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'restaurant_detail_modifications'", 'to': "orm['auth.User']"}),
            'modified_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'restaurant_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'service_days': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'service_fee': ('django.db.models.fields.IntegerField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'service_hours_end': ('django.db.models.fields.TimeField', [], {}),
            'service_hours_start': ('django.db.models.fields.TimeField', [], {}),
            'service_type': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        }
    }

    complete_apps = ['restaurant_detail']