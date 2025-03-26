
-- List of all SQL queries (CRUD operations) used throughout the project, organized by table and operation type.

-- ## Table: profiles
--
--    ### Create (INSERT)
--
--
-- Create profile during registration
INSERT INTO profiles (id, email, full_name, department, role, created_at, updated_at)
VALUES ([user_id], [email], [full_name], [department], [role], [timestamp], [timestamp]);

-- Create profile during login if it doesn't exist
INSERT INTO profiles (id, email, full_name, department, role, created_at, updated_at)
VALUES ([user_id], [email], [user_metadata.full_name], [user_metadata.department], [user_metadata.role], [timestamp], [timestamp]);

-- Create minimal profile during form submission if it doesn't exist
INSERT INTO profiles (id, email, created_at, updated_at)
VALUES ([user_id], [user_email], [timestamp], [timestamp]);


-- ### Read (SELECT)

-- Check if profile exists
SELECT id FROM profiles WHERE id = [user_id];

-- Get user profile
SELECT * FROM profiles WHERE id = [user_id];

-- Get creator name for events
SELECT full_name FROM profiles WHERE id = [creator_id];


-- ### Update (UPDATE)


-- Update profile information
UPDATE profiles
SET full_name = [full_name], department = [department], role = [role], avatar_url = [avatar_url], updated_at = [timestamp]
WHERE id = [user_id];


-- ## Table: events
--
--    ### Create (INSERT)

-- Create a new event
INSERT INTO events (creator_id, title, description, deadline, is_active, is_deadline_enforced, created_at, updated_at)
VALUES ([user_id], [title], [description], [deadline], [is_active], [is_deadline_enforced], [timestamp], [timestamp])
RETURNING *;


-- ### Read (SELECT)

-- Get all events
SELECT * FROM events ORDER BY created_at DESC;

-- Get a specific event
SELECT * FROM events WHERE id = [event_id];

-- Get events created by a user
SELECT * FROM events WHERE creator_id = [user_id] ORDER BY created_at DESC;

-- Get events with creator information
SELECT events.*, profiles.full_name
FROM events
         JOIN profiles ON events.creator_id = profiles.id
ORDER BY events.created_at DESC;

-- Get active events where user hasn't submitted yet
SELECT id, title, description, deadline, is_active, creator_id
FROM events
WHERE creator_id != [user_id]
  AND is_active = true
  AND deadline > [current_timestamp]
  AND id NOT IN (SELECT event_id FROM submissions WHERE user_id = [user_id])
ORDER BY deadline ASC;


-- ### Update (UPDATE)


-- Update event details
UPDATE events
SET title = [title], description = [description], deadline = [deadline],
    is_active = [is_active], is_deadline_enforced = [is_deadline_enforced], updated_at = [timestamp]
WHERE id = [event_id];


-- ## Table: form_fields
-- ### Create (INSERT)

-- Add a form field to an event
INSERT INTO form_fields (
    event_id, field_order, field_type, field_label, field_description,
    is_required, default_value, validation_rules, options
)
VALUES (
           [event_id], [field_order], [field_type], [field_label], [field_description],
           [is_required], [default_value], [validation_rules], [options]
       )
RETURNING *;


-- ### Read (SELECT)

-- Get all form fields for an event
SELECT * FROM form_fields WHERE event_id = [event_id] ORDER BY field_order ASC;


-- ### Update (UPDATE)
-- Update a form field
UPDATE form_fields
SET field_type = [field_type], field_label = [field_label], field_description = [field_description],
    is_required = [is_required], options = [options], updated_at = [timestamp]
WHERE id = [field_id];

-- Update field order
UPDATE form_fields SET field_order = [new_order] WHERE id = [field_id];


-- ### Delete (DELETE)
-- Delete a form field
DELETE FROM form_fields WHERE id = [field_id];


-- ## Table: eligibility
--    ### Create (INSERT)

-- Add eligibility criteria to an event
INSERT INTO eligibility (event_id, criteria_type, criteria_value, created_at, updated_at)
VALUES ([event_id], [criteria_type], [criteria_value], [timestamp], [timestamp]);


-- ### Read (SELECT)

-- Get eligibility criteria for an event
SELECT * FROM eligibility WHERE event_id = [event_id];


-- ## Table: submissions
-- ### Create (INSERT)

-- Submit a response to an event
INSERT INTO submissions (event_id, user_id, submission_data, submitted_at, updated_at)
VALUES ([event_id], [user_id], [submission_data], [timestamp], [timestamp]);


-- ### Read (SELECT)

-- Get all submissions for an event
SELECT submissions.*, profiles.email, profiles.full_name, profiles.department, profiles.role
FROM submissions
         JOIN profiles ON submissions.user_id = profiles.id
WHERE event_id = [event_id]
ORDER BY submitted_at DESC;

-- Get a specific submission
SELECT * FROM submissions WHERE id = [submission_id];

-- Get a user's submission for an event
SELECT * FROM submissions
WHERE event_id = [event_id] AND user_id = [user_id];

-- Count submissions for an event
SELECT COUNT(*) FROM submissions WHERE event_id = [event_id];

-- Get events where a user has submitted
SELECT submissions.*, events.*
FROM submissions
         JOIN events ON submissions.event_id = events.id
WHERE submissions.user_id = [user_id]
ORDER BY submissions.submitted_at DESC;


-- ### Delete (DELETE)


-- Delete a submission
DELETE FROM submissions WHERE id = [submission_id];


-- ## Table: reminders


-- ## Table: statistics

-- ## Functions

-- Check if a user is eligible for an event
SELECT is_user_eligible_for_event([user_id], [event_id]);


