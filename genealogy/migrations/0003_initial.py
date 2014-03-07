# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FamilyMember'
        db.create_table(u'genealogy_familymember', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('middle_name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('suffix', self.gf('django.db.models.fields.CharField')(max_length=5, null=True, blank=True)),
            ('maiden_name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('sex', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('birthday', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('mother', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='mother_to', null=True, to=orm['genealogy.FamilyMember'])),
            ('father', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='father_to', null=True, to=orm['genealogy.FamilyMember'])),
        ))
        db.send_create_signal(u'genealogy', ['FamilyMember'])


    def backwards(self, orm):
        # Deleting model 'FamilyMember'
        db.delete_table(u'genealogy_familymember')


    models = {
        u'genealogy.familymember': {
            'Meta': {'object_name': 'FamilyMember'},
            'birthday': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'father': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'father_to'", 'null': 'True', 'to': u"orm['genealogy.FamilyMember']"}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'maiden_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'mother': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'mother_to'", 'null': 'True', 'to': u"orm['genealogy.FamilyMember']"}),
            'sex': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'suffix': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['genealogy']