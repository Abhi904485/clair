
BEGIN;
--
-- Create model Feature
--
CREATE TABLE "feature" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(128) NOT NULL, "namespace_id" integer NOT NULL REFERENCES "namespace" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE UNIQUE INDEX "feature_namespace_id_name_17b84fa2_uniq" ON "feature" ("namespace_id", "name");
CREATE INDEX "feature_namespace_id_978ec5c1" ON "feature" ("namespace_id");
COMMIT;
BEGIN;
--
-- Create model Featureversion
--
CREATE TABLE "featureversion" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "version" varchar(128) NOT NULL, "feature_id" integer NOT NULL REFERENCES "feature" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE UNIQUE INDEX "featureversion_feature_id_version_75e438ad_uniq" ON "featureversion" ("feature_id", "version");
CREATE INDEX "featureversion_feature_id_234c5ec2" ON "featureversion" ("feature_id");
COMMIT;
BEGIN;
--
-- Create model Keyvalue
--
CREATE TABLE "keyvalue" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "key" varchar(128) NOT NULL UNIQUE, "value" text NULL);
COMMIT;
BEGIN;
--
-- Create model Layer
--
CREATE TABLE "layer" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(128) NOT NULL UNIQUE, "engineversion" smallint NOT NULL, "created_at" datetime NULL, "namespace_id" integer NULL REFERENCES "namespace" ("id") DEFERRABLE INITIALLY DEFERRED, "parent_id" integer NULL REFERENCES "layer" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "layer_namespace_id_91fc5b12" ON "layer" ("namespace_id");
CREATE INDEX "layer_parent_id_801d5dc8" ON "layer" ("parent_id");
COMMIT;
BEGIN;
--
-- Create model LayerDiffFeatureversion
--
CREATE TABLE "layer_diff_featureversion" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "modification" text NOT NULL, "featureversion_id" integer NOT NULL REFERENCES "featureversion" ("id") DEFERRABLE INITIALLY DEFERRED, "layer_id" integer NOT NULL REFERENCES "layer" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE UNIQUE INDEX "layer_diff_featureversion_layer_id_featureversion_id_0a10134a_uniq" ON "layer_diff_featureversion" ("layer_id", "featureversion_id");
CREATE INDEX "layer_diff_featureversion_featureversion_id_98559ccb" ON "layer_diff_featureversion" ("featureversion_id");
CREATE INDEX "layer_diff_featureversion_layer_id_1dc64573" ON "layer_diff_featureversion" ("layer_id");
COMMIT;
BEGIN;
--
-- Create model Lock
--
CREATE TABLE "lock" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(64) NOT NULL UNIQUE, "owner" varchar(64) NOT NULL, "until" datetime NULL);
COMMIT;
BEGIN;
--
-- Create model Namespace
--
CREATE TABLE "namespace" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(128) NULL UNIQUE, "version_format" varchar(128) NULL);
COMMIT;
BEGIN;
--
-- Create model SchemaMigrations
--
CREATE TABLE "schema_migrations" ("version" integer NOT NULL PRIMARY KEY);
COMMIT;
BEGIN;
--
-- Create model Vulnerability
--
CREATE TABLE "vulnerability" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(128) NOT NULL, "description" text NULL, "link" varchar(128) NULL, "severity" text NOT NULL, "metadata" text NULL, "created_at" datetime NULL, "deleted_at" datetime NULL, "severity_source" varchar(128) NULL, "namespace_id" integer NOT NULL REFERENCES "namespace" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "vulnerability_namespace_id_633e520f" ON "vulnerability" ("namespace_id");
COMMIT;
BEGIN;
--
-- Create model VulnerabilityAffectsFeatureversion
--
CREATE TABLE "vulnerability_affects_featureversion" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "featureversion_id" integer NOT NULL REFERENCES "featureversion" ("id") DEFERRABLE INITIALLY DEFERRED, "fixedin_id" integer NOT NULL REFERENCES "vulnerability_fixedin_feature" ("id") DEFERRABLE INITIALLY DEFERRED, "vulnerability_id" integer NOT NULL REFERENCES "vulnerability" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE UNIQUE INDEX "vulnerability_affects_featureversion_vulnerability_id_featureversion_id_01b8566c_uniq" ON "vulnerability_affects_featureversion" ("vulnerability_id", "featureversion_id");
CREATE INDEX "vulnerability_affects_featureversion_featureversion_id_61dd9416" ON "vulnerability_affects_featureversion" ("featureversion_id");
CREATE INDEX "vulnerability_affects_featureversion_fixedin_id_a696b08b" ON "vulnerability_affects_featureversion" ("fixedin_id");
CREATE INDEX "vulnerability_affects_featureversion_vulnerability_id_da4b95e8" ON "vulnerability_affects_featureversion" ("vulnerability_id");
COMMIT;
BEGIN;
--
-- Create model VulnerabilityFixedinFeature
--
CREATE TABLE "vulnerability_fixedin_feature" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "version" varchar(128) NOT NULL, "feature_id" integer NOT NULL REFERENCES "feature" ("id") DEFERRABLE INITIALLY DEFERRED, "vulnerability_id" integer NOT NULL REFERENCES "vulnerability" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE UNIQUE INDEX "vulnerability_fixedin_feature_vulnerability_id_feature_id_dca6722d_uniq" ON "vulnerability_fixedin_feature" ("vulnerability_id", "feature_id");
CREATE INDEX "vulnerability_fixedin_feature_feature_id_019f64fa" ON "vulnerability_fixedin_feature" ("feature_id");
CREATE INDEX "vulnerability_fixedin_feature_vulnerability_id_c311eb20" ON "vulnerability_fixedin_feature" ("vulnerability_id");
COMMIT;
BEGIN;
--
-- Create model VulnerabilityNotification
--
CREATE TABLE "vulnerability_notification" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(64) NOT NULL UNIQUE, "created_at" datetime NULL, "notified_at" datetime NULL, "deleted_at" datetime NULL, "new_vulnerability_id" integer NULL REFERENCES "vulnerability" ("id") DEFERRABLE INITIALLY DEFERRED, "old_vulnerability_id" integer NULL REFERENCES "vulnerability" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "vulnerability_notification_new_vulnerability_id_6f48b940" ON "vulnerability_notification" ("new_vulnerability_id");
CREATE INDEX "vulnerability_notification_old_vulnerability_id_a70f8e3e" ON "vulnerability_notification" ("old_vulnerability_id");
COMMIT;
