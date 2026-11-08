# A Sketchbook of the Netherlands

Eight places, seen twice. Static travel sketchbook with licensed Commons photographs and original code-authored inline SVG interpretations.

## Open
Open `index.html` in a browser. Runtime is one HTML file plus `photos/`; Google Fonts serves Caveat. All other code is local, with no external JavaScript libraries.

## Controls
Open the cover, use the page selector, click previous/next, drag the lower-right corner left, use left/right arrow keys, or swipe. Home returns to the cover; End opens the closing spread. Pages stack at mobile widths. Reduced motion is respected.

## Sources and licences
See the on-page credits and `sources.json` for each photographer, Commons original and licence. Photos are CC BY / CC BY-SA. Resized JPEGs retain the source licence; each illustration is offered under the corresponding source licence, including share-alike where applicable. Original captions and site code: CC BY 4.0. All illustrations are synthetic, shape-by-shape vector interpretations, never traced or embedded photos. The itinerary is imagined, not personal travel testimony.

## Method
Following [Nelson Lee's Turn Trip Photos Into a Digital Sketchbook](https://nelsonxlee.substack.com/p/turn-your-trip-photos-into-a-digital). Substituted direct SVG/vanilla JavaScript authoring for Claude Code / Opus. First built and inspected cover + Kinderdijk, then completed eight spreads, then refined Amsterdam independently. No private photos.

`prepare.py` downloads selected originals into gitignored `originals/`, creates 1600px JPEGs, and strips common metadata using ffmpeg. Then run `strip_jpeg.py` to remove **all** optional application and comment segments (including ICC profiles), and `verify_photos.py` to check every image. Originals are never modified. `notes.md` holds the captions. `build.py` plus `scene_parts.py` regenerates `index.html`.

The photographs span 2004–2026 and are sequenced by the imagined route rather than pretending to be one chronological trip. Author and licence evidence was checked via the Commons API on 9 November 2026. Provenance is deliberately kept in sidecar records rather than re-embedded in the stripped images.
