-- PostgreSQL schema for Kenosis 0.1

CREATE TABLE sessions (
    id SERIAL PRIMARY KEY,
    session_data JSONB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE parsed_states (
    id SERIAL PRIMARY KEY,
    state_data JSONB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE patterns (
    id SERIAL PRIMARY KEY,
    pattern_data JSONB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE expert_corrections (
    id SERIAL PRIMARY KEY,
    correction_data JSONB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);