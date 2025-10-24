// Define the Video class
class Video {
  constructor(title, uploader, time) {
    this.title = title;
    this.uploader = uploader;
    this.time = time; 
  }

  watch() {
    console.log(`${this.uploader} watched all ${this.time} seconds of ${this.title}!`);
  }
}

// Instantiate two Video instances
const video1 = new Video("JavaScript Basics", "Alice", 300);
const video2 = new Video("CSS Flexbox Tutorial", "Bob", 450);

video1.watch(); 
video2.watch(); 


const videosData = [
  { title: "HTML Crash Course", uploader: "Charlie", time: 200 },
  { title: "Node.js Intro", uploader: "Dana", time: 400 },
  { title: "React Tutorial", uploader: "Eve", time: 600 },
  { title: "Vue.js Guide", uploader: "Frank", time: 350 },
  { title: "Angular Basics", uploader: "Grace", time: 500 }
];

// Instantiate Video objects from the array
const videoInstances = videosData.map(data => new Video(data.title, data.uploader, data.time));

// Loop through array and call watch()
videoInstances.forEach(video => video.watch());
