# X2-Pass Character High-Resolution Rebuild Prompt Logic

## Purpose

This workflow is designed to rebuild a character **from scratch** as two separate, ultra-high-resolution images that can later be aligned and merged in Photoshop or another image editor.

This is **not** an upscale, edit, patch, remix, or continuation of an earlier image. The goal is to create two crops that look like they came from **one single high-resolution photograph**.

The two outputs are:

1. **Upper-body pass**
2. **Lower-body pass**

Both images must preserve the same character, body proportions, camera setup, pose, lighting, garment details, and scale.

---

# Core Rule

> **One character. One pose. One camera. One scale. Two crops. Shared overlap. No drift.**

The upper and lower passes must not be treated as separate interpretations.

They must look like two pieces of the **same exact photograph**.

---

# MASTER TWO-PASS PROMPT

## TWO-PASS ULTRA-HIGH-RESOLUTION CHARACTER REBUILD

Use the supplied references to create a completely fresh character rebuild from scratch.

Do not upscale, edit, modify, patch, repaint, or reuse any previous generated image as the base.

Treat the references only as visual source material for identity, proportions, clothing, footwear, colors, accessories, pose, and other specified details.

The final result must consist of **two separate images** designed for seamless Photoshop merging.

---

## PASS 1: UPPER BODY

Generate a maximum-detail ultra-high-resolution image containing:

- full top of hair
- complete head
- face
- neck
- shoulders
- torso
- arms
- hands if naturally visible
- waist
- waistband
- upper hips
- small portion of upper thighs

### Crop

Start:
- above the top of the hair with comfortable margin

End:
- slightly below the waist
- preferably into the upper hips or upper thighs

Include enough lower-body overlap for compositing.

Do not crop the top of the hair.

---

## PASS 2: LOWER BODY

Generate a maximum-detail ultra-high-resolution image containing:

- a small portion of lower torso
- full waist
- waistband
- hips
- pelvis
- thighs
- knees
- calves
- ankles
- shoes
- full soles

### Crop

Start:
- slightly above the waist

End:
- below the shoes with comfortable margin

Do not crop:
- waistband
- knees
- ankles
- toe boxes
- heels
- bottoms of shoes

---

# OVERLAP REQUIREMENT

Use approximately **15-20% overlap** between the two files.

Ideal overlap region:

- lower torso
- shirt hem
- waist
- waistband
- belt
- belt loops
- jean button
- fly
- side seams
- top of pockets
- hands near hips
- upper hip contours

Do not split exactly at the waistline.

The overlap must contain enough visual landmarks to make Photoshop alignment easy.

---

# ALIGNMENT LOCK

Both passes must match exactly in:

- pose
- body rotation
- camera angle
- focal length
- lens perspective
- camera height
- camera distance
- body scale
- centerline
- waist height
- pelvis position
- torso length
- leg length
- head-to-body ratio
- stance
- foot position
- hand position
- garment placement
- lighting
- shadow direction
- background
- rendering style

The two outputs should look like crops taken from a single photograph.

Do not resize the character between passes.

Do not reinterpret the lower body independently.

---

# MASTER CHARACTER SPECIFICATION

Before generating either pass, lock the character's measurements and proportions.

Preserve:

- total apparent height
- head size relative to body
- neck length
- shoulder width
- torso length
- ribcage scale
- waist position
- waist width
- hip width
- pelvis height
- upper leg length
- knee height
- lower leg length
- ankle position
- shoe size
- stance width
- posture
- body angle

If proportion changes are requested, apply them consistently to the full character model before generating either pass.

---

# REFERENCE PRIORITY SYSTEM

When multiple references are supplied, use the highest-detail image for each category.

## Face Priority

Use close-up headshots as the highest authority for:

- identity
- face shape
- eye shape
- eye color
- eyebrow shape
- nose
- lips
- jawline
- skin tone
- skin texture
- hairline
- hairstyle
- earrings
- expression

Do not allow a lower-resolution full-body image to override a high-resolution headshot.

---

## Body Priority

Use the clearest full-body or multi-angle body reference for:

- height
- torso-to-leg ratio
- shoulder width
- waist
- hips
- thighs
- calves
- overall silhouette
- body rotation
- stance
- posture

If multiple body views are available, reconcile them into one consistent three-dimensional character model.

---

## Garment Priority

Use garment close-ups when provided.

They control:

- fabric
- seams
- stitching
- neckline
- sleeve shape
- hem
- logos
- distressing
- trims
- wrinkles
- fabric tension
- color blocking

---

## Footwear Priority

If a dedicated shoe reference exists, it overrides the shoes visible in older body references.

Match:

- overall silhouette
- toe box
- tongue
- laces
- eyelets
- mesh
- cages
- side panels
- heel
- midsole
- outsole
- logos
- stitching
- color placement
- proportions

The footwear must remain the correct scale relative to the legs and body.

---

## Logo Priority

If a separate logo reference is supplied, use it as the highest authority.

Match:

- geometry
- proportions
- outline
- fill
- distress pattern
- stroke thickness
- relative placement
- color

Do not redesign the logo.

---

# EXACT COLOR LOCKING

If the user provides a hexadecimal color, treat it as a hard design value.

Examples:

- `#007474`
- `#D10000`

Apply exact color values consistently across all intended matching elements, such as:

- shirt sleeves
- shirt lettering
- logos
- shoes
- trims
- stitching
- hair ties
- accessories

Do not shift hue, saturation, or brightness between passes unless natural lighting requires extremely subtle variation.

---

# CAMERA LOCK

Both passes must use the same virtual camera.

Lock:

- focal length
- perspective
- subject distance
- camera height
- vertical position
- horizon
- body centerline
- lens compression
- rotation
- view angle

Supported examples:

- front view
- 3/4 front view
- side profile
- 3/4 rear view
- rear view
- custom angle

If Pass 1 uses a 3/4 angle, Pass 2 must use the exact same 3/4 angle.

---

# POSE LOCK

Preserve the same pose across both passes.

Match:

- shoulder angle
- torso twist
- spine posture
- pelvis rotation
- pelvic tilt
- hip shift
- arm position
- hand position
- leg spacing
- knee bend
- weight distribution
- foot rotation

If the character places more weight on one leg, preserve that weight distribution in both passes.

---

# SCALE LOCK

The upper and lower images must use the same apparent scale.

Critical rule:

> **Do not generate the lower pass as a new body. Continue the body established by the master character specification.**

Match:

- waist width
- hip width
- thigh width
- leg length
- knee position
- calf length
- shoe size

The two images should align without proportional resizing.

---

# GARMENT CONTINUITY

Clothing must behave as one continuous garment across both passes.

Preserve:

- fabric texture
- seam locations
- stitching
- wrinkles
- stretch
- drape
- hems
- waistband
- pocket position
- belt position
- logo position
- texture scale
- shading

Do not allow fabric construction to change between the two images.

---

# LIGHTING LOCK

Use the same studio lighting setup for both passes.

Match:

- key-light direction
- fill-light level
- shadow softness
- specular highlights
- skin highlights
- garment highlights
- floor shadows
- exposure
- contrast
- white balance

The two passes must look as if photographed seconds apart in the same studio.

---

# BACKGROUND LOCK

Recommended:

- pure white seamless studio backdrop
- soft natural floor contact shadow
- clean high-key lighting

Keep identical:

- background brightness
- gradient
- floor tone
- shadow density
- horizon behavior

No background clutter.

---

# PHOTOREALISM TARGET

Render as high-end large-format studio photography.

Target qualities:

- realistic skin pores
- fine baby hairs
- individual eyebrow hairs
- natural eyelashes
- believable lip texture
- realistic hair strands
- natural fabric fibers
- accurate seams
- real stitching
- realistic shoe materials
- subtle skin variation
- physically plausible shadows
- clean anatomy
- coherent perspective

Avoid:

- plastic skin
- over-smoothing
- painterly rendering
- CGI appearance
- cartoon style
- AI blur
- distorted anatomy
- duplicated details
- melted logos
- inconsistent fingers
- warped shoes
- mismatched lighting

---

# FRESH REBUILD RULE

Every pass must be created from scratch.

Do not:

- upscale the source image
- clone the source
- patch a previous generation
- reuse a prior image as a hidden base
- inherit previous scene geometry
- preserve old mistakes
- continue from an earlier generation unless explicitly requested

Use the supplied references only as visual guidance.

---

# COMPOSITION RULES

Each pass must be delivered as a separate standalone image.

Do not create:

- collage
- contact sheet
- split screen
- side-by-side layout
- before/after layout
- multiple poses in one file

PASS 1 and PASS 2 must be independent files.

---

# QUALITY PRIORITY ORDER

When conflicts occur, prioritize in this order:

1. identity accuracy
2. body proportion accuracy
3. scale consistency between passes
4. camera consistency
5. pose consistency
6. garment continuity
7. footwear accuracy
8. logo accuracy
9. exact color matching
10. photorealistic detail
11. background continuity

---

# READY-TO-PASTE TEMPLATE

## TWO-PASS ULTRA-HIGH-RESOLUTION CHARACTER REBUILD PROMPT

Create a completely new photorealistic character reconstruction from scratch using only the references supplied with this request.

Do not upscale, edit, modify, repaint, or reuse a previous image as the base.

Create exactly two separate images intended to be merged later in Photoshop.

### Character
[CHARACTER DESCRIPTION]

### View Angle
[FRONT / 3-4 FRONT / SIDE / 3-4 REAR / REAR / CUSTOM]

### Identity Reference
Use the highest-resolution headshot as the primary source for:
- facial identity
- skin tone
- eyes
- nose
- lips
- jawline
- hairline
- hairstyle
- earrings
- expression

### Body Reference
Use the full-body reference for:
- body proportions
- overall height
- torso length
- shoulder width
- waist
- hips
- thighs
- leg length
- stance
- posture

### Outfit
[OUTFIT DESCRIPTION]

### Shoes
Use the dedicated shoe reference as the sole footwear authority.

Ignore shoes from older body references if they conflict.

Match:
- silhouette
- panel layout
- mesh
- sole
- heel
- laces
- tongue
- logos
- color placement

### Logos
Use the dedicated logo reference exactly.

### Exact Colors
[HEX VALUES]

Treat these as locked colors.

### Body Adjustments
[OPTIONAL BODY CHANGES]

Apply requested adjustments to the master body model before generating either pass.

Do not allow Pass 1 and Pass 2 to interpret proportions differently.

---

## IMAGE 1: UPPER BODY

Generate the upper-body image from the top of the hair to slightly below the waist.

Include:
- complete hair
- complete head
- face
- shoulders
- torso
- arms
- hands if visible
- waist
- waistband
- upper hips
- small upper-thigh overlap

Do not crop the top of the hair.

---

## IMAGE 2: LOWER BODY

Generate the lower-body image from slightly above the waist to below the feet.

Include:
- lower torso overlap
- full waist
- waistband
- hips
- pelvis
- thighs
- knees
- calves
- ankles
- complete shoes
- full soles

Do not crop the shoes.

---

## ALIGNMENT

Use approximately 15-20% overlap around the waist and upper hips.

Both images must preserve identical:

- camera angle
- lens
- perspective
- body scale
- rotation
- centerline
- pose
- waist position
- hip position
- lighting
- background
- clothing
- textures
- colors
- rendering style

The two images must look like two crops from the same photograph.

Do not resize the character between passes.

Do not independently reinterpret the lower body.

---

## PHOTOGRAPHIC QUALITY

Render as ultra-high-resolution professional studio photography with:

- realistic skin texture
- natural pores
- fine hair strands
- realistic fabric texture
- precise seams
- accurate stitching
- believable shoe construction
- physically plausible shadows
- clean anatomy
- coherent perspective
- pure white seamless background
- natural floor contact shadows

Avoid:
- cartoon appearance
- CGI appearance
- over-smoothed skin
- distorted anatomy
- warped logos
- inaccurate shoes
- inconsistent colors
- extra fingers
- collage layouts
- visible crop errors

---

## FINAL GOAL

The two images should be mergeable in Photoshop with minimal or no resizing.

When aligned using the overlap region, the character should form one seamless full-body portrait with consistent anatomy, scale, camera perspective, clothing, lighting, and identity.
