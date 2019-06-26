================================
System Requirement Specification
================================

Introduction
============

The purpose of this document is to provide a set of requirements for the Palindrome application. The intended
audience are business users, developers and testers that have an interest in what the application can and can not do.

Features
========

The application only supports one two features: message handling and palindrome checks.

Message Handling
----------------

The message handling functionality allows for messages to be created, retrieved, updated and deleted.

MSG-001 The system must support CRUD operations for messages
    Storage of messages should be persistent, and existing messages should be editable.

MSG-002 The system must support listing messages
    Supports browsing/navigating to messages which the client is not aware of the identity.

Palindrome Checks
-----------------

The palindrome functionality adds to the message handling functionality the ability to check if a particular
message is a palindrome or not. Special for this functionality is being able to determine if it is a strict or relaxed.

PAL-001 The system must support checking if a string is a strict palindrome
    A strict palindrome is a string which character by character, is a palindrome. This includes spaces, special
    characters and so on. This is typically what computers consider a palindrome.

PAL-002 The system must support checking if a string is a relaxed palindrome.
    A relaxed palindrome is a string in which alphanumeric characters are the same, disregarding spaces, special
    characters and so on. This is typically what people consider a palindrome.

Data Requirements
=================

Data Model
----------

The key data object in the solution is the message. It consists of a character string. Every message must have
the following fields.

id (integer)
    The identification number of the message. Used for identifying a message when retrieving, updating and deleting.
    Positive integer value.

message (string)
    The message body itself.

is_strict_palindrome (boolean)
    The status flag indicating if a palindrome is strict or not.

is_relaxed_palindrome (boolean)
    The status flag indicating if a palindrome is relaxed or not.

created (timestamp)
    The creation timestamp for the message.

last_modified (timestamp)
    The last modified timestamp for the message. Useful to see when a message was last changed.


External Interface Requirements
===============================

The following external interface requirements exists

Web Service API
---------------

There is a requirement for the web service to have a public API.

WEB-001 The system must provide CRUD operations via a RESTful API
    Aligned with the project brief.

WEB-002 The system may provide a browseable user interface
    Added for convenience.

WEB-003 The system must exchange information in JSON format
    Assumed from the project brief.


Quality Attributes
==================

Quality attribute analysis has been moved to the corresponding section in the Architecture Description. This section
only contains the key non-functional requirements. The list of quality attributes are aligned with the list in the book
Software Requirements (Wiegers & Beatty).

External Quality Attributes
---------------------------

Availability
^^^^^^^^^^^^

No availability requirements.

Installability
^^^^^^^^^^^^^^

INSTALL-001 The system may be containerized
    The project brief mentions that the software may be containerized to demonstrate that it can be packaged
    appropriately.

Integrity
^^^^^^^^^

No integrity requirements.

Interoperability
^^^^^^^^^^^^^^^^

INTEROP-001 The system must have a web service interface
    This is discussed more in detail under the external interface requirements section.

Performance
^^^^^^^^^^^

No performance requirements.

Reliability
^^^^^^^^^^^

No reliability requirements.

Robustness
^^^^^^^^^^

No robustness requirements.

Safety
^^^^^^

No safety requirements.

Security
^^^^^^^^

No security requirements. (See architecture description for more information.)

Usability
^^^^^^^^^

No usability requirements. (Project brief says to avoid focusing on any UI.)

Internal Quality Attributes
---------------------------

Efficiency
^^^^^^^^^^

EFF-001 The system should minimize CPU load of palindrome checks
    We do not want to spend precious CPU cycles checking of a message is a palindrome. (Assumed that this
    operation is expensive.)

Modifiability
^^^^^^^^^^^^^

No modifiability requirements.

Portability
^^^^^^^^^^^

PORT-001 The system should be able to execute on Windows, Linux and Mac
    This gives us more options when it comes to deployment as we don't know what operating system the reviewers
    are on.

Reusability
^^^^^^^^^^^

No reusability requirements.

Scalability
^^^^^^^^^^^

SCALE-001 The system should be able to scale horizontally
    Being a web service, it should be able to scale if load increases.

Verifiability
^^^^^^^^^^^^^

No verifiability requirements.


