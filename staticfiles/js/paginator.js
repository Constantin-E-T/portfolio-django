$(document).ready(function() {
    $('.load-more').click(function(e) {
        e.preventDefault();
        var link = $(this).attr('href');
        $.get(link, function(data) {
            // Parse the HTML response
            var html = $.parseHTML(data);
            // Extract the news articles and the "Load More" button
            var news = $(html).find('.blog-item');
            var loadMore = $(html).find('.load-more');
            // Insert the news articles into the page
            $('.blog-item').last().after(news);
            // Update the "Load More" button's link
            if (loadMore.length > 0) {
                $('.load-more').attr('href', loadMore.attr('href'));
            } else {
                $('.load-more').remove();
            }
        });
    });
});
