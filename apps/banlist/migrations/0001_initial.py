# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UserBanList'
        db.create_table(u'banlist_userbanlist', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('plain_type', self.gf('django.db.models.fields.CharField')(default='default', max_length=64)),
            ('reason', self.gf('django.db.models.fields.CharField')(max_length=4096, null=True, blank=True)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=datetime.datetime.now, blank=True)),
            ('updated_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=datetime.datetime.now, blank=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accounts.User'])),
            ('nickname', self.gf('django.db.models.fields.CharField')(max_length=512)),
        ))
        db.send_create_signal(u'banlist', ['UserBanList'])

        # Adding model 'ServerBanList'
        db.create_table(u'banlist_serverbanlist', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('plain_type', self.gf('django.db.models.fields.CharField')(default='default', max_length=64)),
            ('reason', self.gf('django.db.models.fields.CharField')(max_length=4096, null=True, blank=True)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=datetime.datetime.now, blank=True)),
            ('updated_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=datetime.datetime.now, blank=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accounts.User'])),
            ('ip_address', self.gf('django.db.models.fields.IPAddressField')(max_length=15)),
            ('server_name', self.gf('django.db.models.fields.CharField')(max_length=512, null=True, blank=True)),
        ))
        db.send_create_signal(u'banlist', ['ServerBanList'])


    def backwards(self, orm):
        # Deleting model 'UserBanList'
        db.delete_table(u'banlist_userbanlist')

        # Deleting model 'ServerBanList'
        db.delete_table(u'banlist_serverbanlist')


    models = {
        u'accounts.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invites': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
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
        u'banlist.serverbanlist': {
            'Meta': {'ordering': "['created_on']", 'object_name': 'ServerBanList'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounts.User']"}),
            'plain_type': ('django.db.models.fields.CharField', [], {'default': "'default'", 'max_length': '64'}),
            'reason': ('django.db.models.fields.CharField', [], {'max_length': '4096', 'null': 'True', 'blank': 'True'}),
            'server_name': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'datetime.datetime.now', 'blank': 'True'})
        },
        u'banlist.userbanlist': {
            'Meta': {'ordering': "['created_on']", 'object_name': 'UserBanList'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounts.User']"}),
            'plain_type': ('django.db.models.fields.CharField', [], {'default': "'default'", 'max_length': '64'}),
            'reason': ('django.db.models.fields.CharField', [], {'max_length': '4096', 'null': 'True', 'blank': 'True'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'datetime.datetime.now', 'blank': 'True'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['banlist']