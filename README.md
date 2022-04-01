# Kent Maps Images

This repository contains image files and metadata used by the [Kent Maps Online](https://kent-maps.online) web site

The image files and metadata are used in the generation of [IIIF](https://iiif.io) manifests that are used by the [Juncture](https://juncture-digital.org) service that powers the Kent Maps site.

# The International Image Interoperability Framework (IIIF)

[IIIF](https://iiif.io) is a set of open standards for delivering high-quality, attributed digital objects online at scale. It’s also an international community developing and implementing the IIIF APIs. IIIF is backed by a consortium of leading cultural institutions.

The metadata in this repository are used to generate manifest files that are compliant with the [IIIF Presentation API 3.0](https://iiif.io/api/presentation/3.0/).  Detailed knowledge of IIIF is not needed to contribute or use images in this repository.

In many cases a minimal set of IIIF required metadata for a single image can be inferred from site-wide default values and image-specific metadata that can be inferred from the image file name (such as the image title and reuse rights).

In situations where more descriptive metadata is needed a simple key-value properties file can be associated with a single image or a group of images located in a folder.

# Options for image and/or metadata hosting

## 1) Image only

The easiest method for hosting a file is to simply upload the image file in this repository using a file name that can be used to generate the image label (caption) and can optionally includes a reuse rights code.

When using this method the image file name represents the image label and an optional segment that consists of a reuse rights code.  The label and rights code segments are separated by the first `-` character in the file name.  All spaces in the label segment of the file name must be converted to underscore (`_`) characters.  A double underscore (`__`) can be used to signify the end of a title.  This can be useful if multiple images in a folder will use the same label.  For instance, `Some_label__1-CC0.jpg` and `Some_label__2-CC0.jpg`.  In this example both image files have a unique file name but can be associated with the same label and rights code.

The reuse rights for an image is defined by appending a Creative Commons or Rights Statements code to the end of the file name (but before the file extension).  The reuse rights code is one of the [Creative Commons](https://creativecommons.org/licenses/) or [RightsStatements.org](https://rightsstatements.org/page/1.0/) codes defined in [Reuse Rights](#reuse-rights) section below.  If a rights code is not provided in the file name a default value is used.  The default value is obtained from properties files found in the folder heirarchy in which the image file is located.  If rights metadata is available in multiple properties files the value in the file that is closest to the image takes precedence.  For instance, if a properties file at the root of the repository defined the reuse rights as `CC BY` and then another properties file in a parent/ancestor folder of the image defined the reuse rights as `CC BY-SA`, the `CC BY SA` value would take precedence and would be used in the generated IIIF manifest.

### Examples

The image file [Fallstaff_Hotel_and_Westgate_Towers,_Canterbury-CC0.jpg](Fallstaff_Hotel_and_Westgate_Towers,_Canterbury-CC0.jpg) would result in an IIIF manifest that can be accessed via the URL [https://iiif.visual-essays.net/gh:kent-map/images/Fallstaff_Hotel_and_Westgate_Towers,_Canterbury-CC0.jpg/manifest.json](https://iiif.visual-essays.net/gh:kent-map/images/Fallstaff_Hotel_and_Westgate_Towers,_Canterbury-CC0.jpg/manifest.json).  This manifest can then be used in any IIIF viewer to view the image.  For instance, [https://iiif.visual-essays.net/gh:kent-map/images/Fallstaff_Hotel_and_Westgate_Towers,_Canterbury-CC0.jpg](https://iiif.visual-essays.net/gh:kent-map/images/Fallstaff_Hotel_and_Westgate_Towers,_Canterbury-CC0.jpg).

## 2) Image and properties file

In situations where it is desired to associate richer metadata with an image a supplemental properties file may be used.

### Examples

The image [Dane_John_Park.jpg](Dane_John_Park.jpg) is accompanied with the [Dane_John_Park.yaml](Dane_John_Park.yaml) which includes a summary, date, and Wikidata QID (in the `depicts` metadata field).  The `depicts` metadata property can be used to indentify entities depicted in the image.  In this example the included Wikidata QID (Q16988443) indicates that the [Dane John Mound](https://en.wikipedia.org/wiki/Dane_John_Mound) is depicted in the image.
The IIIF manifest for this image can be seen at [https://iiif.visual-essays.net/gh:kent-map/images/Dane_John_Park.jpg/manifest.json](https://iiif.visual-essays.net/gh:kent-map/images/Dane_John_Park/manifest.json).  The image can be viewed in the visual-essays.net image viewer at [https://iiif.visual-essays.net/gh:kent-map/images/Dane_John_Park](https://iiif.visual-essays.net/gh:kent-map/images/Dane_John_Park).

## 3) Properties file only

In situations where an image is hosted on another web site that does not provide a IIIF manifest a properties file is used to define the IIIF metadata in a generated IIIF manifest.  In this situation the URL to the externally hosted image is included in the properties file in addition to the usual IIIF metadata properties.

### Examples

TODO

# Reuse Rights

The IIIF Presentation Manifests provide a flexible approach for explicitly defining the reuse rights for an image and any attribution (or other) statements that must be displayed when the image is used.

`Rights` refers string that identifies a license or rights statement that applies to the content of the resource, such as the JSON of a Manifest or the pixels of an image. The value must be drawn from the set of [Creative Commons](https://creativecommons.org/licenses/) license URIs or [RightsStatements.org](https://rightsstatements.org/page/1.0/) rights statement URIs

## Creative Commons Licenses

- `CC0`: [Public Domain Dedication](http://creativecommons.org/publicdomain/zero/1.0/)
- `CC-BY`: [Attribution](http://creativecommons.org/licenses/by/4.0/)
- `CC-BY-SA`: [Attribution-ShareAlike](http://creativecommons.org/licenses/by-sa/4.0/)
- `CC-BY-ND`: [Attribution-NoDerivs](http://creativecommons.org/licenses/by-nd/4.0/)
- `CC-BY-NC`: [Attribution-NonCommercial](http://creativecommons.org/licenses/by-nc/4.0/)
- `CC-BY-NC-SA`: [Attribution-NonCommercial](http://creativecommons.org/licenses/by-nc-sa/4.0/)
- `CC-BY-NC-ND`: [Attribution-NonCommercial-NoDerivs](http://creativecommons.org/licenses/by-nc-nd/4.0/)

## Rights Statements

- `InC`: [In Copyright](http://rightsstatements.org/vocab/InC/1.0/)
- `InC-OW-EU`: [In Copyright - EU Orphan Work](http://rightsstatements.org/vocab/InC-OW-EU/1.0/)
- `InC-EDU`: [In Copyright - Educational Use Permitted](http://rightsstatements.org/vocab/InC-EDU/1.0/)
- `InC-NC`: [In Copyright - Non-Commercial Use Permitted](http://rightsstatements.org/vocab/InC-NC/1.0/)
- `InC-RUU`: [In Copyright - Rights-Holder(s) Unlocatable or Unidentifiable](http://rightsstatements.org/vocab/InC-RUU/1.0/)
- `NoC-CR`: [No Copyright - Contractual Restrictions](http://rightsstatements.org/vocab/NoC-CR/1.0/)
- `NoC-NC`: [No Copyright - Non-Commercial Use Only](http://rightsstatements.org/vocab/NoC-NC/1.0/)
- `NoC-OKLR`: [No Copyright - Other Known Legal Restrictions](http://rightsstatements.org/vocab/NoC-OKLR/1.0/)
- `NoC-US`: [No Copyright - United States](http://rightsstatements.org/vocab/NoC-US/1.0/)
- `CNE`: [Copyright Not Evaluated](http://rightsstatements.org/vocab/CNE/1.0/)
- `UND`: [Copyright Undertermined](http://rightsstatements.org/vocab/UND/1.0/)
- `NKC`: [No Known Copyright](http://rightsstatements.org/vocab/NKC/1.0/)

# Defining rights

## Using a file naming convention

The easiest method for defining the rights for an image hosted in Github is to append a Creative Commons or Rights Statements code to the end (but before the file extension) of the Gihub file name.  The naming convention recognized by the Visual Essays IIIF manifest generator splits the file name into two segments.  The segments are separated by the first `-` found in the file name.  The first segment is the image label (or caption) and the second is the rights code.  The rights code is one of the Creative Commons or RightsStatements.org codes defined in the section above.

The text before the first `-` character in the file name is used to create the image label/caption unless this is overridden by a label property in an image-specific properties (`.yaml`) file.  When using the first segment from the file name for the label, any underscore (`_`) charcters are converted to spaces.  A double underscore (`__`) can be used to signify the end of a title.  This can be useful if multiple images in a folder will use the same label.  For instance, `Some_label__1-CC0.jpg` and `Some_label__2-CC0.jpg`.  In this example both image files have a unique file name but can be associated with the same label and rights code.

## Using metadata files

An alternative to adding the rights code to the file name is to associate a metadata file with an image.  The metadata file approach provides a mechanism for defining a wide range of attributes for an image.  A metadata file can be associated with a single image or all images contained in a folder.

### Associating metadata with a single image

Metadata can be associated with a single image by creating a `.yaml` file with the same root file name as the image but with the `.yaml` extension instead of the image extenstion (typically `.jpg` or `.png`).  For instance, to associate a metadata file with the image named `Fiordo_de_Furore.jpg` the file `Fiordo_de_Furore.yaml` would be created in the same directory. 

### Associating metadata with multiple images

Metadata can be associated with multiple files by grouping the files in a folder and adding a `metadata.yaml` file in the same folder.

# Image metadata file format

Metadata files for single images or groups of images in a folder follow the structure defined for the [IIIF Presentation API v3.0](https://iiif.io/api/presentation/3.0/#42-resource-representations).  The [iiif-props.template.yaml][iiif-props.template.yaml] can be copied and used as a starter for folder or image-level properties. 

# Using a metadata file for external files

In addition to defining metadata for files hosted in Github, metadata files may also be used to associate metadata (for manifest generation) with files hosted on other sites.  An example of this can be seen with the [Westgate_today.yaml][images/kent-maps/Westgate_today.yaml] file.

- https://iiif.visual-essays.net/gh:rdsnyder/examples/images/kent-maps/Westgate_today

# Examples

## Defining rights using the file naming convention

### Open Access Images with Public Domain Dedication (Creative Commons CC0)

- https://iiif.visual-essays.net/gh:rdsnyder/examples/images/Italy_2022/Positano-CC0.jpg

### Open Access Images with Attribution Requirement (Creative Commons CC BY)

- https://iiif.visual-essays.net/gh:rdsnyder/examples/images/Italy_2022/Vernazza-CC-BY.png

## Defining rights and other properties with image properties file

- https://iiif.visual-essays.net/gh:rdsnyder/examples/images/Italy_2022/Fiordo_de_Furore.jpg
- https://iiif.visual-essays.net/gh:rdsnyder/examples/images/plant-humanities/Babur_supervising_laying_out.jpg
- https://iiif.visual-essays.net/gh:rdsnyder/examples/images/plant-humanities/Grave_of_Justina_Davis_Nash.jpg
- https://iiif.visual-essays.net/gh:rdsnyder/examples/images/plant-humanities/Mughal_style_tamarind.png
- https://iiif.visual-essays.net/gh:rdsnyder/examples/images/plant-humanities/Heliconia_chartacea.yaml


## Defining rights and other properties with folder properties file

- https://iiif.visual-essays.net/gh:rdsnyder/examples/images/Italy_2022/Riomaggiore_sunset.jpg
- https://iiif.visual-essays.net/gh:rdsnyder/examples/images/Italy_2022/Pompeii/Pompeii__1.jpg
- https://iiif.visual-essays.net/gh:rdsnyder/examples/images/Italy_2022/Pompeii/Pompeii__2.jpg
