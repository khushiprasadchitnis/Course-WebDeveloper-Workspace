const puppeteer = require('puppeteer');
const path = require('path');
const fs = require('fs');

(async () => {
    const inputFilePath = process.argv[2];
    const outputFilePath = process.argv[3];

    if (!fs.existsSync(inputFilePath)) {
        console.error('Input file does not exist.');
        process.exit(1);
    }

    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    const absolutePath = path.resolve(inputFilePath);
    const fileUrl = `file://${absolutePath}`;
    await page.goto(fileUrl, { waitUntil: 'networkidle2' });
    await page.screenshot({ path: outputFilePath });
    await browser.close();
})();

