# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'NewsTranslation'
        db.create_table('news_news_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('content', self.gf('django.db.models.fields.CharField')(max_length=8192, null=True, blank=True)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['news.News'])),
        ))
        db.send_create_signal('news', ['NewsTranslation'])

        # Adding unique constraint on 'NewsTranslation', fields ['language_code', 'master']
        db.create_unique('news_news_translation', ['language_code', 'master_id'])

        # Adding model 'News'
        db.create_table('news_news', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('updated_on', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now_add=True, blank=True)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now=True, blank=True)),
        ))
        db.send_create_signal('news', ['News'])


    def backwards(self, orm):
        # Removing unique constraint on 'NewsTranslation', fields ['language_code', 'master']
        db.delete_unique('news_news_translation', ['language_code', 'master_id'])

        # Deleting model 'NewsTranslation'
        db.delete_table('news_news_translation')

        # Deleting model 'News'
        db.delete_table('news_news')


    models = {
        'news.news': {
            'Meta': {'object_name': 'News'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'})
        },
        'news.newstranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'NewsTranslation', 'db_table': "'news_news_translation'"},
            'content': ('django.db.models.fields.CharField', [], {'max_length': '8192', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': "orm['news.News']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['news']