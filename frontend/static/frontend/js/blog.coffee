blogId = "3771681492165373124"

apiKey = "AIzaSyDj73DQJINLQE5DDuvBekrqBmLUDvA0uc0"

getUrl = "https://www.googleapis.com/blogger/v3/blogs/" + blogId + "/posts?key=" + apiKey

buildItemHtml = (item) ->
    result = "<h2>" + item.title + "</h2>"
    result += "<p>By <a target=\"_blank\" href=\"" + item.author.url + "\">" + item.author.displayName + "</a> "
    result += "on " + new Date(item.published).toDateString() + "</p>"
    result += "<p>" + item.content + "</p>"
    return result

loadBlog = () ->
    $.getJSON getUrl, (data) ->
        target = $ ".js-blog-posts"
        for item in data.items
            target.append(buildItemHtml item)

$(document).ready () ->
    loadBlog()
