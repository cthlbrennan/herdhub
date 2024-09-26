/* jshint esversion: 11 */

/**
 * @jest-environment jsdom
 */

// Jest testing based on 
// https://www.testim.io/blog/jest-testing-a-helpful-introductory-tutorial/

const { test, expect } = require("@jest/globals");
const fs = require("fs");
const path = require("path");

function loadHtmlFile(filename) {
    const filePath = path.resolve(__dirname, `../../../templates/${filename}`);
    let fileContents = fs.readFileSync(filePath, "utf-8");
    
    // Replace Django template tags with placeholder values
    fileContents = fileContents.replace(/{%\s*static\s*'([^']*)'\s*%}/g, "$1");
    fileContents = fileContents.replace(/{%\s*csrf_token\s*%}/g, "");
    fileContents = fileContents.replace(/{%\s*form\.as_p\s*%}/g, `
        <label for="id_comments">Comments</label>
        <textarea id="id_comments"></textarea>
        <input type="date">
    `);

    document.open();
    document.write(fileContents);
    document.close();
}

describe('Home Page Tests', () => {
    beforeAll(() => {
        loadHtmlFile("index.html");
    });

    test('should have hero image element', () => {
        const heroImageHome = document.getElementById('hero-image');
        expect(heroImageHome).not.toBeNull();
        expect(heroImageHome.hasAttribute('data-image-url')).toBe(true);
    });
});

describe('About Page Tests', () => {
    beforeAll(() => {
        loadHtmlFile("about.html");
    });

    test('should have about image element', () => {
        const heroImageAbout = document.getElementById('about-image');
        expect(heroImageAbout).not.toBeNull();
        expect(heroImageAbout.hasAttribute('data-image-url')).toBe(true);
    });
});

describe('Add Cow Page Tests', () => {
    beforeAll(() => {
        loadHtmlFile("add_cow.html");
    });

    test('should add <br> before comments <textarea>', () => {
        const commentsLabel = document.querySelector('label[for="id_comments"]');
        if (commentsLabel) {
            const lineBreak = commentsLabel.nextSibling;
            expect(lineBreak.tagName).toBe('BR');
        } else {
            console.warn('Element label[for="id_comments"] not found in the DOM');
        }
    });

    test('should set max date for date input fields to today', () => {
        const dateInputs = document.querySelectorAll('input[type="date"]');
        const today = new Date().toISOString().split("T")[0];
        dateInputs.forEach(input => {
            expect(input.getAttribute("max")).toBe(today);
        });
    });
});