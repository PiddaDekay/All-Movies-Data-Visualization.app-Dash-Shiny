#
# This is a Shiny web application. You can run the application by clicking
# the 'Run App' button above.
#
# Find out more about building applications with Shiny here:
#
#    http://shiny.rstudio.com/
#

library(shiny)

# Define UI for application that draws a histogram
ui <- fluidPage(
  titlePanel("My Simple App"),
  
  sidebarLayout(
    sidebarPanel(
      helpText("Controls for my app"),
      
      selectInput("fruitchoice", 
                  label = "Choose a fruit",
                  choices = list("Apples", 
                                 "Oranges",
                                 "Mangos", 
                                 "Pomegranate"),
                  selected = "Percent White"),
      
      sliderInput("amt", 
                  label = "Order Amount:",
                  min=0, max = 100, value=20),
      
      actionButton("goButton", "Update Order")
      
      ),

    
    mainPanel(
      helpText("Fruit Chosen:"),
      verbatimTextOutput("fruit"),
      helpText("Order Amount"),
      verbatimTextOutput("amt")
    )
  )
)

# Define server logic required to draw a histogram
server <- function(input, output) {
   display1 <- eventReactive(input$goButton,{input$fruitchoice})
   display2 <- eventReactive(input$goButton,{input$amt})
   output$fruit <- renderText({display1()})
   output$amt <- renderText({display2()})
}

# Run the application 
shinyApp(ui = ui, server = server)

