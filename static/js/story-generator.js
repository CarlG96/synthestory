document.addEventListener('DOMContentLoaded', event => {
    console.log('working');
    let storyStart = `{{ story_start }} {{ story_middle }} {{ story_end }}`;
    console.log(storyStart);
    document.getElementById("id_story_text").setAttribute("value", storyStart);
})