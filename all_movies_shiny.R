#
# This is a Shiny web application. You can run the application by clicking
# the 'Run App' button above.
#
# Find out more about building applications with Shiny here:
#
#    http://shiny.rstudio.com/
#

library(shiny)
library(ggplot2)
# data processing
data = read.csv("all_movies.csv")
df <- subset(data,select = c('Rated','Year','Genre','Rating10','Rotten','BoxOffice'))
df[df==''] <-NA
df <- na.omit(df)
genre_set = unique(df['Genre'])
genre_list=c()
for (i in 0:dim(genre_set)[1]){
    for (j in 0:length(unlist(strsplit(genre_set[i,1],', ')))){
        genre_list <- c(genre_list,unlist(strsplit(genre_set[i,1],', '))[j])
    }
}
genre_list <- unique(genre_list)
rating <- unique(df['Rated'])


# Define UI for application that draws a histogram
ui <- fluidPage(
    titlePanel("Movie Revenue Analysis"),
    
    sidebarLayout(
        sidebarPanel(
            helpText("Controls for my app"),
            
            selectInput("genre", 
                        label = "Choose a genre",
                        choices = list('All','Drama', 'History', 'Sci-Fi', 'Crime', 'Thriller', 'War',
                                       'Film-Noir', 'Adventure', 'Family', 'Fantasy', 'Comedy', 'Romance',
                                       'Mystery', 'Western', 'Action', 'Musical', 'Horror', 'Biography',
                                       'Music', 'Documentary', 'Animation', 'Sport', 'Short', 'News'),
                        selected = "Percent White"),
            
            sliderInput("range_of_year", 
                        label = "Range of Year",
                        min=min(df['Year']), max = max(df['Year']), value=c(min(df['Year']),max(df['Year']))),
            
            selectInput("rating", 
                        label = "Choose a rating",
                        choices = list('All','Unrated', 'Not Rated', 'Approved', 'PG', 'PG-13', 'R', 'G',
                                       'NC-17', 'TV-PG', 'Atp', 'MA15+'),
                        selected = "Percent White"),
            
            
            
        ),
        
        
        mainPanel(
            fluidRow(
                column(6,plotOutput("distPlot",width="300px",height="300px")),
                column(6,plotOutput("distPlot2",width="300px",height="300px"))
            )
        )
    )
)

# Define server logic required to draw a histogram
server <- function(input, output) {
    
    output$distPlot <- renderPlot({
        if(input$genre=='All'){
            if(input$rating=='All'){
                x1=subset(df,(Year>=input$range_of_year[1])&(Year<=input$range_of_year[2]))
            }
            else{
                x1=subset(df,((Year>=input$range_of_year[1])&(Year<=input$range_of_year[2]))&(Rated==input$rating))
            }
        }
        else{
            if(input$rating=='All'){
                x1=subset(df,(Year>=input$range_of_year[1])&(Year<=input$range_of_year[2])&grepl(input$genre,Genre))
            }
            else{
                x1 = subset(df,((Year>=input$range_of_year[1])&(Year<=input$range_of_year[2])) & (Rated==input$rating) & grepl(input$genre,Genre))
            }
        }
        #dataframe
        xnew1 <- x1[order(x1$Rating10),]
        plot1 <- data.frame(xnew1['Rating10'],xnew1['BoxOffice'])
        
        #plot
        ggplot(plot1, aes(x=Rating10, y=BoxOffice,)) +
            geom_point(size=3)
    })
    output$distPlot2 <- renderPlot({
        if(input$genre=='All'){
            if(input$rating=='All'){
                x2=subset(df,(Year>=input$range_of_year[1])&(Year<=input$range_of_year[2]))
            }
            else{
                x2=subset(df,((Year>=input$range_of_year[1])&(Year<=input$range_of_year[2]))&(Rated==input$rating))
            }
        }
        else{
            if(input$rating=='All'){
                x2=subset(df,(Year>=input$range_of_year[1])&(Year<=input$range_of_year[2])&grepl(input$genre,Genre))
            }
            else{
                x2 = subset(df,((Year>=input$range_of_year[1])&(Year<=input$range_of_year[2])) & (Rated==input$rating) & grepl(input$genre,Genre))
            }
        }
        
        #dataframe
        xnew2 <- x2[order(x2$Rating10),]
        plot2 <- data.frame(xnew2['Rotten'],xnew2['BoxOffice'])
        
        #plot
        ggplot(plot2, aes(x=Rotten, y=BoxOffice,)) +
            geom_point(size=3)
    })
}

# Run the application 
shinyApp(ui = ui, server = server)

