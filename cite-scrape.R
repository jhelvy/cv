source("functions.R")

# Store IDs
gscholar_id <- 'DY2D56IAAAAJ'
gscholar_page <- paste0("https://scholar.google.com/citations?user=", gscholar_id)

sheet <- get_cv_sheet('pubs')
id <- sheet %>%
    filter(!is.na(id_scholar)) %>%
    pull(id_scholar)
id <- id[1]
url <- paste0(
    "https://scholar.google.com/citations?view_op=view_citation&hl=en&user=DY2D56IAAAAJ&citation_for_view=DY2D56IAAAAJ:",
    id
)



html <- xml2::read_html(url)
rvest::html_elements(html, ".gs_scl") %>%
    html_elements('a') %>%
    html_text2()


library(httr)
page <- GET(url)
page_content <- str_to_lower(content(page, as = "text"))
str_split(page_content, 'cited by')[[1]]

