# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Release.sha'
        db.alter_column(u'stretch_release', 'sha', self.gf('django.db.models.fields.CharField')(max_length=28))

    def backwards(self, orm):

        # Changing field 'Release.sha'
        db.alter_column(u'stretch_release', 'sha', self.gf('django.db.models.fields.CharField')(max_length=40))

    models = {
        u'stretch.deploy': {
            'Meta': {'object_name': 'Deploy'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'environment': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'deploys'", 'to': u"orm['stretch.Environment']"}),
            'existing_release': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'deploy_existing_releases'", 'null': 'True', 'to': u"orm['stretch.Release']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'release': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'deploy_releases'", 'null': 'True', 'to': u"orm['stretch.Release']"}),
            'task_id': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'})
        },
        u'stretch.environment': {
            'Meta': {'object_name': 'Environment'},
            'auto_deploy': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'current_release': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stretch.Release']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'system': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'environments'", 'to': u"orm['stretch.System']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'using_source': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'stretch.group': {
            'Meta': {'object_name': 'Group'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'environment': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'groups'", 'to': u"orm['stretch.Environment']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'load_balancer': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['stretch.LoadBalancer']", 'unique': 'True', 'null': 'True'}),
            'maximum_nodes': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'minimum_nodes': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'node': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stretch.Node']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'})
        },
        u'stretch.host': {
            'Meta': {'object_name': 'Host'},
            'address': ('django.db.models.fields.GenericIPAddressField', [], {'max_length': '39'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'domain_name': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'environment': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'hosts'", 'to': u"orm['stretch.Environment']"}),
            'fqdn': ('django.db.models.fields.TextField', [], {'unique': 'True'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'hosts'", 'null': 'True', 'to': u"orm['stretch.Group']"}),
            'hostname': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'})
        },
        u'stretch.instance': {
            'Meta': {'object_name': 'Instance'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'environment': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'instances'", 'to': u"orm['stretch.Environment']"}),
            'host': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'instances'", 'to': u"orm['stretch.Host']"}),
            'id': ('uuidfield.fields.UUIDField', [], {'unique': 'True', 'max_length': '32', 'primary_key': 'True'}),
            'node': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'instances'", 'to': u"orm['stretch.Node']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'})
        },
        u'stretch.loadbalancer': {
            'Meta': {'object_name': 'LoadBalancer'},
            'address': ('django.db.models.fields.GenericIPAddressField', [], {'max_length': '39'}),
            'backend_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'}),
            'host_port': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'port': ('django.db.models.fields.IntegerField', [], {}),
            'protocol': ('django.db.models.fields.TextField', [], {})
        },
        u'stretch.node': {
            'Meta': {'object_name': 'Node'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'ports': ('jsonfield.fields.JSONField', [], {}),
            'system': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'nodes'", 'to': u"orm['stretch.System']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'})
        },
        u'stretch.portbinding': {
            'Meta': {'object_name': 'PortBinding'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'destination': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instance': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'port_bindings'", 'to': u"orm['stretch.Instance']"}),
            'source': ('django.db.models.fields.IntegerField', [], {}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'})
        },
        u'stretch.release': {
            'Meta': {'object_name': 'Release'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'sha': ('django.db.models.fields.CharField', [], {'max_length': '28'}),
            'system': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'releases'", 'to': u"orm['stretch.System']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'})
        },
        u'stretch.service': {
            'Meta': {'object_name': 'Service'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'data': ('jsonfield.fields.JSONField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'system': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'services'", 'to': u"orm['stretch.System']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'})
        },
        u'stretch.system': {
            'Meta': {'object_name': 'System'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'domain_name': ('django.db.models.fields.TextField', [], {'unique': 'True', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {'unique': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['stretch']