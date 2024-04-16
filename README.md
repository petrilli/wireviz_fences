# Wireviz Fences

Support for Wireviz notation inside of superfences.

# Features

* Basic support and rendering inline of SVG version of the
  [Wireviz](https://github.com/wireviz/WireViz) diagram. This
  is done in the most basic fashion, but it plugs the pieces together.

## Usage

This is mostly for use with MkDocs, and you can add it to your configuration
(`mkdocs.yml`) with:

```yaml
markdown_extensions:
  - pymdownx.superfences:
      custom_fences:
        - name: wireviz
          class: wireviz
          format: !!python/name:wireviz_fences.fence_wireviz
```

You can then mark your fenced area with `wireviz` and it will automatically
be formatted correctly.
