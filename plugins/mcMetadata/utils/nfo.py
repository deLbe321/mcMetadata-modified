import os

INDENTED_NEWLINE = "\n    "


def build_nfo_xml(scene, settings):
    ret = """<?xml version="1.0" encoding="utf-8" standalone="yes"?>
<movie>
    <name>{title}</name>
    <title>{title}</title>
    <originaltitle>{title}</originaltitle>
    <sorttitle>{title}</sorttitle>
    <director>{director}</director>
    <{default_rating}>{rating}</{default_rating}>
    <plot><![CDATA[{details}]]></plot>
    <premiered>{date}</premiered>
    <releasedate>{date}</releasedate>
    <year>{year}</year>
    <studio>{studio}</studio>{performers}
    <genre>{genre}</genre>{tags}
    <uniqueid type="stash">{id}</uniqueid>
</movie>"""

    default_rating = settings.get("default_rating", "userrating")
    genre = settings.get("genre", "Adult")
    id = scene["id"]
    details = scene["details"] or ""

    title = ""
    if scene["title"] is not None and scene["title"] != "":
        title = scene["title"]
    else:
        title = os.path.basename(os.path.normpath(scene["files"][0]["path"]))

    rating = ""
    if scene["rating100"] is not None:
        rating = round(int(scene["rating100"]) / 10)

    date = ""
    year = ""
    if scene["date"] is not None:
        date = scene["date"]
        year = scene["date"].split("-")[0]

    studio = ""
    if scene["studio"] is not None:
        studio = scene["studio"]["name"]
    
    director = ""
    if scene["director"] is not None:
        director = scene["director"]

    performers = INDENTED_NEWLINE
    i = 0

    for p in scene["performers"]:
        if i != 0:
            performers = performers + INDENTED_NEWLINE
        performers = (
            performers
            + """<actor>
        <name>{}</name>
        <role>{}</role>
        <order>{}</order>
        <type>Actor</type>
    </actor>""".format(p["name"], p["name"], i)
        )
        i += 1
    if performers == INDENTED_NEWLINE:
        performers = ""

    tags = INDENTED_NEWLINE
    iTwo = 0
    for t in scene["tags"]:
        if iTwo != 0:
            tags = tags + INDENTED_NEWLINE
        tags = tags + """<tag>{}</tag>""".format(t["name"])
        iTwo += 1
    if tags == INDENTED_NEWLINE:
        tags = ""

    return ret.format(
        title=title,
        director=director,
        default_rating=default_rating,
        rating=rating,
        genre=genre,
        id=id,
        tags=tags,
        date=date,
        year=year,
        studio=studio,
        performers=performers,
        details=details,
    )
