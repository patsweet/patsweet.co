# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FamilyMember'
        db.create_table(u'family_tree_familymember', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('maiden_name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('birthday', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('mother', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='mother_to', null=True, to=orm['family_tree.FamilyMember'])),
            ('father', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='father_to', null=True, to=orm['family_tree.FamilyMember'])),
        ))
        db.send_create_signal(u'family_tree', ['FamilyMember'])


    def backwards(self, orm):
        # Deleting model 'FamilyMember'
        db.delete_table(u'family_tree_familymember')


    models = {
        u'family_tree.familymember': {
            'Meta': {'object_name': 'FamilyMember'},
            'birthday': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'father': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'father_to'", 'null': 'True', 'to': u"orm['family_tree.FamilyMember']"}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'maiden_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'mother': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'mother_to'", 'null': 'True', 'to': u"orm['family_tree.FamilyMember']"})
        }
    }

    complete_apps = ['family_tree']