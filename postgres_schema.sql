BEGIN;
--
-- Create model Feature
--
CREATE TABLE "feature" ("id" serial NOT NULL PRIMARY KEY, "name" varchar(128) NOT NULL, "namespace_id" integer NOT NULL);
ALTER TABLE "feature" ADD CONSTRAINT "feature_namespace_id_name_17b84fa2_uniq" UNIQUE ("namespace_id", "name");
ALTER TABLE "feature" ADD CONSTRAINT "feature_namespace_id_978ec5c1_fk_namespace_id" FOREIGN KEY ("namespace_id") REFERENCES "namespace" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "feature_namespace_id_978ec5c1" ON "feature" ("namespace_id");
COMMIT;
BEGIN;
--
-- Create model Featureversion
--
CREATE TABLE "featureversion" ("id" serial NOT NULL PRIMARY KEY, "version" varchar(128) NOT NULL, "feature_id" integer NOT NULL);
ALTER TABLE "featureversion" ADD CONSTRAINT "featureversion_feature_id_version_75e438ad_uniq" UNIQUE ("feature_id", "version");
ALTER TABLE "featureversion" ADD CONSTRAINT "featureversion_feature_id_234c5ec2_fk_feature_id" FOREIGN KEY ("feature_id") REFERENCES "feature" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "featureversion_feature_id_234c5ec2" ON "featureversion" ("feature_id");
COMMIT;
BEGIN;
--
-- Create model Keyvalue
--
CREATE TABLE "keyvalue" ("id" serial NOT NULL PRIMARY KEY, "key" varchar(128) NOT NULL UNIQUE, "value" text NULL);
CREATE INDEX "keyvalue_key_4fef3488_like" ON "keyvalue" ("key" varchar_pattern_ops);
COMMIT;
BEGIN;
--
-- Create model Layer
--
CREATE TABLE "layer" ("id" serial NOT NULL PRIMARY KEY, "name" varchar(128) NOT NULL UNIQUE, "engineversion" smallint NOT NULL, "created_at" timestamp with time zone NULL, "namespace_id" integer NULL, "parent_id" integer NULL);
ALTER TABLE "layer" ADD CONSTRAINT "layer_namespace_id_91fc5b12_fk_namespace_id" FOREIGN KEY ("namespace_id") REFERENCES "namespace" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "layer" ADD CONSTRAINT "layer_parent_id_801d5dc8_fk_layer_id" FOREIGN KEY ("parent_id") REFERENCES "layer" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "layer_name_a6ac4656_like" ON "layer" ("name" varchar_pattern_ops);
CREATE INDEX "layer_namespace_id_91fc5b12" ON "layer" ("namespace_id");
CREATE INDEX "layer_parent_id_801d5dc8" ON "layer" ("parent_id");
COMMIT;
BEGIN;
--
-- Create model LayerDiffFeatureversion
--
CREATE TABLE "layer_diff_featureversion" ("id" serial NOT NULL PRIMARY KEY, "modification" text NOT NULL, "featureversion_id" integer NOT NULL, "layer_id" integer NOT NULL);
ALTER TABLE "layer_diff_featureversion" ADD CONSTRAINT "layer_diff_featureversio_layer_id_featureversion__0a10134a_uniq" UNIQUE ("layer_id", "featureversion_id");
ALTER TABLE "layer_diff_featureversion" ADD CONSTRAINT "layer_diff_featureve_featureversion_id_98559ccb_fk_featureve" FOREIGN KEY ("featureversion_id") REFERENCES "featureversion" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "layer_diff_featureversion" ADD CONSTRAINT "layer_diff_featureversion_layer_id_1dc64573_fk_layer_id" FOREIGN KEY ("layer_id") REFERENCES "layer" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "layer_diff_featureversion_featureversion_id_98559ccb" ON "layer_diff_featureversion" ("featureversion_id");
CREATE INDEX "layer_diff_featureversion_layer_id_1dc64573" ON "layer_diff_featureversion" ("layer_id");
COMMIT;
BEGIN;
--
-- Create model Lock
--
CREATE TABLE "lock" ("id" serial NOT NULL PRIMARY KEY, "name" varchar(64) NOT NULL UNIQUE, "owner" varchar(64) NOT NULL, "until" timestamp with time zone NULL);
CREATE INDEX "lock_name_d38b9ebb_like" ON "lock" ("name" varchar_pattern_ops);
COMMIT;
BEGIN;
--
-- Create model Namespace
--
CREATE TABLE "namespace" ("id" serial NOT NULL PRIMARY KEY, "name" varchar(128) NULL UNIQUE, "version_format" varchar(128) NULL);
CREATE INDEX "namespace_name_04632cab_like" ON "namespace" ("name" varchar_pattern_ops);
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
CREATE TABLE "vulnerability" ("id" serial NOT NULL PRIMARY KEY, "name" varchar(128) NOT NULL, "description" text NULL, "link" varchar(128) NULL, "severity" text NOT NULL, "metadata" text NULL, "created_at" timestamp with time zone NULL, "deleted_at" timestamp with time zone NULL, "severity_source" varchar(128) NULL, "namespace_id" integer NOT NULL);
ALTER TABLE "vulnerability" ADD CONSTRAINT "vulnerability_namespace_id_633e520f_fk_namespace_id" FOREIGN KEY ("namespace_id") REFERENCES "namespace" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "vulnerability_namespace_id_633e520f" ON "vulnerability" ("namespace_id");
COMMIT;
BEGIN;
--
-- Create model VulnerabilityAffectsFeatureversion
--
CREATE TABLE "vulnerability_affects_featureversion" ("id" serial NOT NULL PRIMARY KEY, "featureversion_id" integer NOT NULL, "fixedin_id" integer NOT NULL, "vulnerability_id" integer NOT NULL);
ALTER TABLE "vulnerability_affects_featureversion" ADD CONSTRAINT "vulnerability_affects_fe_vulnerability_id_feature_01b8566c_uniq" UNIQUE ("vulnerability_id", "featureversion_id");
ALTER TABLE "vulnerability_affects_featureversion" ADD CONSTRAINT "vulnerability_affect_featureversion_id_61dd9416_fk_featureve" FOREIGN KEY ("featureversion_id") REFERENCES "featureversion" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "vulnerability_affects_featureversion" ADD CONSTRAINT "vulnerability_affect_fixedin_id_a696b08b_fk_vulnerabi" FOREIGN KEY ("fixedin_id") REFERENCES "vulnerability_fixedin_feature" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "vulnerability_affects_featureversion" ADD CONSTRAINT "vulnerability_affect_vulnerability_id_da4b95e8_fk_vulnerabi" FOREIGN KEY ("vulnerability_id") REFERENCES "vulnerability" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "vulnerability_affects_featureversion_featureversion_id_61dd9416" ON "vulnerability_affects_featureversion" ("featureversion_id");
CREATE INDEX "vulnerability_affects_featureversion_fixedin_id_a696b08b" ON "vulnerability_affects_featureversion" ("fixedin_id");
CREATE INDEX "vulnerability_affects_featureversion_vulnerability_id_da4b95e8" ON "vulnerability_affects_featureversion" ("vulnerability_id");
COMMIT;
BEGIN;
--
-- Create model VulnerabilityFixedinFeature
--
CREATE TABLE "vulnerability_fixedin_feature" ("id" serial NOT NULL PRIMARY KEY, "version" varchar(128) NOT NULL, "feature_id" integer NOT NULL, "vulnerability_id" integer NOT NULL);
ALTER TABLE "vulnerability_fixedin_feature" ADD CONSTRAINT "vulnerability_fixedin_fe_vulnerability_id_feature_dca6722d_uniq" UNIQUE ("vulnerability_id", "feature_id");
ALTER TABLE "vulnerability_fixedin_feature" ADD CONSTRAINT "vulnerability_fixedin_feature_feature_id_019f64fa_fk_feature_id" FOREIGN KEY ("feature_id") REFERENCES "feature" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "vulnerability_fixedin_feature" ADD CONSTRAINT "vulnerability_fixedi_vulnerability_id_c311eb20_fk_vulnerabi" FOREIGN KEY ("vulnerability_id") REFERENCES "vulnerability" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "vulnerability_fixedin_feature_feature_id_019f64fa" ON "vulnerability_fixedin_feature" ("feature_id");
CREATE INDEX "vulnerability_fixedin_feature_vulnerability_id_c311eb20" ON "vulnerability_fixedin_feature" ("vulnerability_id");
COMMIT;
