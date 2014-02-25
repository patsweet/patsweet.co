# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'FamilyMember.suffix_name'
        db.delete_column(u'family_tree_familymember', 'suffix_name')

        # Adding field 'FamilyMember.suffix'
        db.add_column(u'family_tree_familymember', 'suffix',
                      self.gf('django.db.models.fields.CharField')(max_length=5, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'FamilyMember.suffix_name'
        db.add_column(u'family_tree_familymember', 'suffix_name',
                      self.gf('django.db.models.fields.CharField')(max_length=5, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'FamilyMember.suffix'
        db.delete_column(u'family_tree_familymember', 'suffix')


    models = {
        u'family_tree.familymember': {
            'Meta': {'object_name': 'FamilyMember'},
            'birthday': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'father': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'father_to'", 'null': 'True', 'to': u"orm['family_tree.FamilyMember']"}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'maiden_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'mother': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'mother_to'", 'null': 'True', 'to': u"orm['family_tree.FamilyMember']"}),
            'sex': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'suffix': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['family_tree']