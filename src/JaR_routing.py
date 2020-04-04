import JaR_templating

# !!------------- NEEDS SECURITY TESTING -----------------
# path checing is done AFTER the routng part => "empty" or "/" is not allowed
def isAllowed(path, prepath):
    if path=="/favicon.ico": # favicon is enabled
        return (True, 200)
    p = path.split("/")
    for k in p: # Probably handled on browser side. STILL NEEDED!
        if k.strip() == "..": #no ".."s are allowed
            return (False, 403)
    if p[0].strip() != "": # Probably handled on browser side.
        return (False, 404)
    # allowed directories:
    allow = {"templates", "img", "css", "temp", "js", "fonts"} # temp=temporary
    if JaR_templating.fileOrDirExists(prepath + path): # if the file exists:
        if p[1] in allow:
            return (True, 200) # file exists and is not forbidden
    else: # if there is no such file:
        return (False, 404)
    # if the file is not in the allowed folders (but exists):
    return (False, 403)


# Do PARAMS NEED SEC CHECKING???

routes = {
    "": "/templates/index.html",
    "/" : "/templates/index.html",
    "/nyil": "/img/arrow6.png"
}

# If the routing path is not in "routes", return the unchanged routing path:
# Note that the routing path is already stripped
def getFilePathEnding(routing_path):
    return routes.get(routing_path, routing_path)


