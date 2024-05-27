# Web Development Fundamentals
# By TACHI YASSINE

## General

### What is HTML
HTML (HyperText Markup Language) is the standard markup language used to create web pages. It describes the structure of a webpage using a series of elements or tags.

### How to create an HTML page
To create an HTML page, you need to use HTML tags to define the structure and content of the page. The basic structure includes the `<!DOCTYPE html>`, `<html>`, `<head>`, and `<body>` tags.

### What is a markup language
A markup language is a system for annotating a document in a way that is syntactically distinguishable from the text. HTML is an example of a markup language used to structure content on the web.

### What is the DOM
The Document Object Model (DOM) is a programming interface for web documents. It represents the page so that programs can change the document structure, style, and content. The DOM represents the document as a tree of nodes.

### What is an element / tag
An HTML element is a part of a webpage defined by a start tag, any content, and an end tag. For example, `<p>This is a paragraph.</p>` is a paragraph element.

### What is an attribute
An attribute provides additional information about an HTML element. Attributes are always included in the opening tag and usually come in name/value pairs, such as `class="classname"`.

### How does the browser load a webpage
When you enter a URL in a browser, it sends a request to the web server. The server responds with the requested HTML file, which the browser parses. The browser then builds the DOM tree, applies CSS styles, executes JavaScript, and finally renders the page.

## CSS

### What is CSS
CSS (Cascading Style Sheets) is a stylesheet language used to describe the presentation of a document written in HTML or XML. CSS defines how elements should be displayed on the screen, on paper, or in other media.

### How to add style to an element
Styles can be added to HTML elements using inline styles, internal stylesheets, or external stylesheets. Inline styles are added directly within an element's tag using the `style` attribute. Internal styles are defined within the `<style>` tag in the HTML document's `<head>`. External stylesheets are linked using the `<link>` tag.

### What is a class
A class is an attribute in HTML used to define a group of elements. It allows you to apply CSS styles to multiple elements simultaneously. For example, `<div class="container">...</div>`.

### What is a selector
A CSS selector is a pattern used to select the elements you want to style. It can be an element name, class name, ID, or any combination thereof.

### How to compute CSS Specificity Value
CSS specificity determines which styles are applied to an element when there are multiple conflicting rules. Specificity is calculated based on the types of selectors used: inline styles have the highest specificity, followed by IDs, classes/attributes/pseudo-classes, and finally, element tags.

### What are Box properties in CSS
Box properties in CSS define the layout and spacing of elements on a webpage. These properties include `margin`, `border`, `padding`, and `width/height`. They determine the space around, between, and within elements.
