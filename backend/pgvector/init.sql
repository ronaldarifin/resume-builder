\c matcher

CREATE EXTENSION vector;

CREATE TABLE employers (
    employer_name character varying(100),
    job_embedding vector(384)
);

CREATE TABLE transfer_data (
    id integer NOT NULL,
    resume_file_hash character varying(200)
);

CREATE SEQUENCE resume_scores_id_seq;

CREATE TABLE resume_scores (
    id integer NOT NULL DEFAULT nextval('resume_scores_id_seq'::regclass),
    candidate_name character varying(100),
    resume_embedding vector(384),
    PRIMARY KEY (id)
);



