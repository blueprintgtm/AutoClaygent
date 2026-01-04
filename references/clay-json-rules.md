# Clay JSON Rules

Full specification for valid JSON schemas in Clay (OpenAI Structured Outputs).

---

## 1. Root-Level Structure

- The root of every JSON output must be a single JSON object: `{}`
- The root object cannot be an array or any other type
- The root schema must not use `anyOf` at the top level

---

## 2. Supported JSON Types

**Allowed JSON value types:**
- `string`
- `number`
- `integer`
- `boolean`
- `object`
- `array`
- `null` (only via anyOf if used as an optional type)
- `enum`
- `anyOf` (only for fields, not root)

**Disallowed types/keywords:**
- `oneOf`, `allOf`, `not`
- `if/then/else`
- `format`, `default`, `const`, `examples`
- `patternProperties`, `propertyNames`
- `unevaluatedProperties`
- `contains`, `dependencies`

---

## 3. Required vs Optional Fields

- All JSON fields in Clay schemas must be **explicitly required**
- Optional fields must be represented using `anyOf` with null

**Example:**
```json
"field_name": {
  "anyOf": [
    { "type": "string" },
    { "type": "null" }
  ]
}
```

---

## 4. Objects & Additional Properties

- All objects must include: `"additionalProperties": false`
- This prohibits undeclared keys
- Explicitly list all expected properties; do not allow free-form object content

---

## 5. Arrays

- Arrays must be properly formatted: `[value1, value2, ...]`
- Array elements must be valid JSON values of allowed types

---

## 6. Enum Limits

- Enum values must be valid primitives: strings, numbers, or booleans
- If an enum contains over 250 values:
  - Total character length of the enum values must not exceed 7,500 characters

---

## 7. Property Name & Schema Size Limits

- Maximum combined length of all property names: **15,000 characters**
- Maximum total properties across the full schema: **100**
- Maximum depth of nesting: **5 levels**
- Schemas must include `additionalProperties: false` at all object levels

---

## 8. Value Constraints (No Data Validation Rules)

Clay uses structure, not value validation:

**Do NOT include value constraints like:**
- `minLength`, `maxLength`, `pattern`
- `minimum`, `maximum`, `exclusiveMinimum`, `exclusiveMaximum`
- `dependencies`, `dependentRequired`, `dependentSchemas`

No regex-based or format checks are allowed.

---

## 9. Booleans & Nulls

- Booleans must be `true` or `false` (not `"Yes"`/`"No"`)
- Nulls must be explicit `null` values, not empty strings

**Correct:**
```json
"online_signup": null
"works_with_employers": true
```

**Incorrect:**
```json
"online_signup": ""
"works_with_employers": "Yes"
```

---

## 10. JSON Validation Rules (Syntax)

- Strings must use double quotes
- No trailing commas anywhere
- Numbers must be legitimate JSON numbers
- Arrays and objects must be syntactically correct

---

## 11. anyOf Usage

- `anyOf` may only be used at the **field level**, never at the root
- `anyOf` is commonly used for optional fields: Field is either `<type>` OR `null`

**Example:**
```json
"billing_vendor": {
  "anyOf": [
    { "type": "string" },
    { "type": "null" }
  ]
}
```

---

## 12. Disallowed Keywords

The following must not appear in Clay JSON schemas:

- `pattern`, `minLength`, `maxLength`
- `minimum`, `maximum`, `exclusiveMinimum`, `exclusiveMaximum`
- `format`, `const`, `default`, `examples`
- `propertyNames`, `patternProperties`
- `contains`, `if`, `then`, `else`
- `oneOf`, `allOf`, `not`
- `dependencies`, `dependentRequired`
- `unevaluatedProperties`

---

## 13. Purpose & Usage

- These rules are designed for Clay using OpenAI Structured Outputs
- Clay expects predictable output formats
- Anything not conforming will be rejected or parsed incorrectly
- Schemas are structural, not data-constraint validators

---

## Quick Reference: Valid Schema Template

```json
{
  "type": "object",
  "properties": {
    "required_string": {
      "type": "string"
    },
    "optional_string": {
      "anyOf": [
        { "type": "string" },
        { "type": "null" }
      ]
    },
    "required_boolean": {
      "type": "boolean"
    },
    "enum_field": {
      "type": "string",
      "enum": ["option_a", "option_b", "option_c"]
    },
    "nested_object": {
      "type": "object",
      "properties": {
        "inner_field": { "type": "string" }
      },
      "required": ["inner_field"],
      "additionalProperties": false
    }
  },
  "required": ["required_string", "optional_string", "required_boolean", "enum_field", "nested_object"],
  "additionalProperties": false
}
```
