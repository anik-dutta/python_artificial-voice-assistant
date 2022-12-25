const contain = document.getElementById('visualizer-canvas');
const canvas = document.getElementById('mainCanvas');

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;
const ctx = canvas.getContext('2d');

var assisstant_message_count = 0;
var user_message_count = 0;

// Particle Initialization
let particlesArray;
var swap = false;
var mail_enable_check = false; //Mail
var email_check = false;
var sub_per_check = false;
var sub_check = false;
var sub_confirm_check = false;
var text_check = false;
var response = "";
var ass_msg = "";

//Multi-input features' default tag-value
var tag;

//get mouse position
let mouse = {
    x: null,
    y: null,
    radius: (canvas.height / 80) * (canvas.width / 80)
}

window.addEventListener("load", initialassisstantMessageappend(), visualizer());

function changeParticle() {
    createParticle();
}

function changeVisualizer() {
    visualizer();
}

//text mode
function onClick($elem) {
    var _val = $elem.previousElementSibling.value;
    document.getElementById('input-val').value = '';

    if (mail_enable_check == false) {
        userMessageappend(_val);
        assisstantMessageappend(_val);
    } else {
        response = _val;
        mail(tag);
    }
}

//aduio mode
async function change() {
    swap = !swap;

    if (swap == true) {
        document.getElementById("mybtn2").style.backgroundColor = "lightgreen";
        await eel.audio_mode_on()();
    }
    if (swap == false) {
        document.getElementById("mybtn2").style.backgroundColor = "white";
        await eel.audio_mode_off()();
    }
    while (swap == true) {
        msg = await eel.sendResponse_audio()();
        userMessageappend(msg);
        assisstantMessageappend(msg);
    }
}

//add user message
function userMessageappend(message) {
    user_message_count++;
    var months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
    var today = new Date();
    var date = months[today.getMonth()] + " " + (today.getDate());

    root = document.getElementById("conversation-container")

    var user_message = document.createElement('div');
    user_message.id = "user-message" + String(user_message_count);
    user_message.className = "message-row user-message";

    var user_message_text = document.createElement('div');
    user_message_text.className = "message-text";
    user_message_text.innerText = message;

    var user_message_date = document.createElement('div');
    user_message_date.className = "message-date";
    user_message_date.innerHTML = date;

    var userNodes = [user_message_text, user_message_date];
    for (var i = 0; i < userNodes.length; i++) {
        user_message.appendChild(userNodes[i]);
    }
    root.prepend(user_message);
}

//add assisstant message
async function assisstantMessageappend(message) {
    visualizer();

    assisstant_message_count++;
    var months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];

    if (mail_enable_check == false) {
        var _message = await eel.sendResponse(message, swap)();
        tag = _message;
    }
    if (tag == "send email" && swap == false) {
        if (mail_enable_check == false && email_check == false && sub_per_check == false && sub_check == false && text_check == false) {
            mail_enable_check = true;
            email_check = true;
            sub_per_check = true
            sub_check = true;
            text_check = true;
        }
        mail(tag);
    } else {
        var today = new Date();
        var _date = months[today.getMonth()] + " " + (today.getDate());

        root = document.getElementById("conversation-container")

        var assisstant_message = document.createElement('div');
        assisstant_message.id = "assisstant-message" + String(assisstant_message_count);
        assisstant_message.className = "message-row assisstant-message";

        var assisstant_message_content = document.createElement('div');
        assisstant_message_content.className = "message-content";

        var assisstant_img = document.createElement('img');
        assisstant_img.src = "images/nexus2cee_Hound-Thumb.png";
        assisstant_img.alt = "assisstant-logo";
        assisstant_img.width = "25";
        assisstant_img.height = "25";

        var assisstant_message_text = document.createElement('div');
        assisstant_message_text.className = "message-text";
        assisstant_message_text.innerText = _message;

        var assisstant_message_date = document.createElement('div');
        assisstant_message_date.className = "message-date";
        assisstant_message_date.innerText = _date;

        var assisstantNodes = [assisstant_img, assisstant_message_text, assisstant_message_date];
        for (var i = 0; i < assisstantNodes.length; i++) {
            assisstant_message_content.appendChild(assisstantNodes[i]);
        }
        assisstant_message.appendChild(assisstant_message_content);

        root.prepend(assisstant_message);
    }
}

//initail assisstant response
async function initialassisstantMessageappend() {
    visualizer();

    assisstant_message_count++;
    var months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
    var _message = await eel.initialResponse()();
    var today = new Date();
    var _date = months[today.getMonth()] + " " + (today.getDate());

    root = document.getElementById("conversation-container")

    var assisstant_message = document.createElement('div');
    assisstant_message.id = "assisstant-message" + String(assisstant_message_count);
    assisstant_message.className = "message-row assisstant-message";

    var assisstant_message_content = document.createElement('div');
    assisstant_message_content.className = "message-content";

    var assisstant_img = document.createElement('img');
    assisstant_img.src = "images/nexus2cee_Hound-Thumb.png";
    assisstant_img.alt = "assisstant-logo";
    assisstant_img.width = "25";
    assisstant_img.height = "25";

    var assisstant_message_text = document.createElement('div');
    assisstant_message_text.className = "message-text";
    assisstant_message_text.innerText = _message;

    var assisstant_message_date = document.createElement('div');
    assisstant_message_date.className = "message-date";
    assisstant_message_date.innerText = _date;

    var assisstantNodes = [assisstant_img, assisstant_message_text, assisstant_message_date];
    for (var i = 0; i < assisstantNodes.length; i++) {
        assisstant_message_content.appendChild(assisstantNodes[i]);
    }
    assisstant_message.appendChild(assisstant_message_content);

    root.prepend(assisstant_message);
}

//Mail
async function mail(tag) {
    if (mail_enable_check == true && email_check == true && sub_per_check == true && sub_check == true && text_check == true) {
        msg = await eel.askEmail(tag)();
        mail_assisstantMessageappend(msg);
        email_check = false;
    } else if (mail_enable_check == true && email_check == false && sub_per_check == true && sub_check == true && text_check == true) {
        userMessageappend(response);
        await eel.addEmail(tag, response)();
        ass_msg = await eel.askSubjectPermission(tag)();
        mail_assisstantMessageappend(ass_msg);
        sub_per_check = false;
    } else if (mail_enable_check == true && email_check == false && sub_per_check == false && sub_check == true && text_check == true) {
        userMessageappend(response);
        ass_msg = await eel.askSubject(tag, response)();
        ass_msg = String(ass_msg);
        if (ass_msg.includes("//*yes//*") == true) {
            sub_confirm_check = true;
            ass_msg = ass_msg.replace(",//*yes//*", " ");
        } else if (ass_msg.includes("//*no//*") == true) {
            sub_confirm_check = false;
            ass_msg = ass_msg.replace(",//*no//*", " ");
        }
        mail_assisstantMessageappend(ass_msg);
        sub_check = false;
    } else if (mail_enable_check == true && email_check == false && sub_per_check == false && sub_check == false && sub_confirm_check == true && text_check == true) {
        userMessageappend(response);
        await eel.addSubject(tag, response)();
        ass_msg = await eel.askText(tag)();
        mail_assisstantMessageappend(ass_msg);
        text_check = false;
    } else if (mail_enable_check == true && email_check == false && sub_per_check == false && sub_check == false && text_check == false) {
        userMessageappend(response);
        await eel.addText(tag, response)();
        ass_msg = await eel.sendEmail(tag)();
        mail_assisstantMessageappend(ass_msg);
        mail_enable_check = false;
    }
    if (mail_enable_check == true && email_check == false && sub_per_check == false && sub_check == false && sub_confirm_check == false && text_check == true) {
        ass_msg = await eel.askText(tag)();
        mail_assisstantMessageappend(ass_msg);
        text_check = false;
    }
}

//Mail assisstant message append
async function mail_assisstantMessageappend(message) {
    visualizer();

    assisstant_message_count++;
    var months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
    var today = new Date();
    var _date = months[today.getMonth()] + " " + (today.getDate());

    root = document.getElementById("conversation-container")

    var assisstant_message = document.createElement('div');
    assisstant_message.id = "assisstant-message" + String(assisstant_message_count);
    assisstant_message.className = "message-row assisstant-message";

    var assisstant_message_content = document.createElement('div');
    assisstant_message_content.className = "message-content";

    var assisstant_img = document.createElement('img');
    assisstant_img.src = "images/nexus2cee_Hound-Thumb.png";
    assisstant_img.alt = "assisstant-logo";
    assisstant_img.width = "25";
    assisstant_img.height = "25";

    var assisstant_message_text = document.createElement('div');
    assisstant_message_text.className = "message-text";
    assisstant_message_text.innerText = message;

    var assisstant_message_date = document.createElement('div');
    assisstant_message_date.className = "message-date";
    assisstant_message_date.innerText = _date;

    var assisstantNodes = [assisstant_img, assisstant_message_text, assisstant_message_date];
    for (var i = 0; i < assisstantNodes.length; i++) {
        assisstant_message_content.appendChild(assisstantNodes[i]);
    }
    assisstant_message.appendChild(assisstant_message_content);

    root.prepend(assisstant_message);
}

//Visualizer
function visualizer() {
    const context = new AudioContext();
    const analyser = new AnalyserNode(context, { fftSize: 1024 });

    setupContext();

    async function setupContext() {
        const source = await getSource();
        if (context.state === 'suspended') {
            await context.resume();
        }
        const contextSource = context.createMediaStreamSource(source);
        contextSource.connect(analyser);
    }

    function getSource() {
        return navigator.mediaDevices.getUserMedia({
            audio: {
                echoCancellation: false,
                autoGainControl: false,
                noiseSuppression: true,
                latency: 0,
                volume: 500
            }
        })
    }

    const bufferLength = analyser.frequencyBinCount;
    const dataArray = new Uint8Array(bufferLength);
    const barWidth = (canvas.width / 2) / bufferLength;
    let barHeight;
    let x;

    function animate() {
        x = 0;
        analyser.getByteFrequencyData(dataArray);
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        drawVisualizer(bufferLength, x, barWidth, barHeight, dataArray);
        requestAnimationFrame(animate);
    }
    animate();
};

function drawVisualizer(bufferLength, x, barWidth, barHeight, dataArray) {
    for (let i = 0; i < bufferLength; i++) {
        barHeight = dataArray[i] * 1.5;
        ctx.save();
        ctx.translate(canvas.width / 2, canvas.height / 2);
        ctx.rotate(i * Math.PI * 10 / bufferLength);
        var hue = i * 0.3;
        ctx.fillStyle = 'hsl(' + hue + ', 100%,' + barHeight / 3 + '%)';
        ctx.fillRect(0, 0, barWidth, barHeight);
        x += barWidth;
        ctx.restore();
    }
}

//Particle Effect
window.addEventListener('mousemove',
    function (event) {
        mouse.x = event.x;
        mouse.y = event.y;
    }
);

function createParticle() {
    //create particle
    class Particle {
        constructor(x, y, directionX, directionY, size, color) {
            this.x = x;
            this.y = y;
            this.directionX = directionX;
            this.directionY = directionY;
            this.size = size;
            this.color = color;
        }

        //method to draw individual particle
        draw() {
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2, false);
            ctx.fillStyle = '#8C5523';
            ctx.fill();
        }

        update() {
            if (this.x > canvas.width || this.x < 0) {
                this.directionX = -this.directionX;
            }
            if (this.y > canvas.height || this.y < 0) {
                this.directionY = -this.directionY;
            }
            //check collison detection - mouse position / particle position
            let dx = mouse.x - this.x;
            let dy = mouse.y - this.y;
            let distance = Math.sqrt(dx * dx + dy * dy);
            if (distance < mouse.radius + this.size) {
                if (mouse.x < this.x && this.x < canvas.width - this.size * 10) {
                    this.x += 10;
                }
                if (mouse.x > this.x && this.x > this.size * 10) {
                    this.x -= 10;
                }
                if (mouse.y < this.y && this.y < canvas.height - this.size * 10) {
                    this.y += 10;
                }
                if (mouse.y > this.y && this.y > this.size * 10) {
                    this.y -= 10;
                }
            }

            //move particle
            this.x += this.directionX;
            this.y += this.directionY;
            //draw particle
            this.draw();
        }
    }

    //create particle array
    function init() {
        particlesArray = [];
        let numberOfParticles = (canvas.height * canvas.width) / 9000;
        for (let i = 0; i < numberOfParticles; i++) {
            let size = (Math.random() * 5) + 1;
            let x = (Math.random() * ((innerWidth - size * 2) - (size * 2)) + size * 2);
            let y = (Math.random() * ((innerHeight - size * 2) - (size * 2)) + size * 2);
            let directionX = (Math.random() * 5) - 2.5;
            let directionY = (Math.random() * 5) - 2.5;
            let color = '#8C5523';

            particlesArray.push(new Particle(x, y, directionX, directionY, size, color));
        }
    }

    //check if particles are close enough to draw line between them
    function connect() {
        let opacityValue = 1;
        for (let a = 0; a < particlesArray.length; a++) {
            for (let b = a; b < particlesArray.length; b++) {
                let distance = ((particlesArray[a].x - particlesArray[b].x) * (particlesArray[a].x - particlesArray[b].x)) + ((particlesArray[a].y - particlesArray[b].y) * (particlesArray[a].y - particlesArray[b].y));
                if (distance < (canvas.width / 7) * (canvas.height / 7)) {
                    opacityValue = 1 - (distance / 20000);
                    ctx.strokeStyle = 'rgba(140,85,31,1' + opacityValue + ')';
                    ctx.lineWidth = 1;
                    ctx.beginPath();
                    ctx.moveTo(particlesArray[a].x, particlesArray[a].y);
                    ctx.lineTo(particlesArray[b].x, particlesArray[b].y);
                    ctx.stroke();
                }
            }
        }
    }

    //animation loop
    function animate() {
        requestAnimationFrame(animate);
        ctx.clearRect(0, 0, innerWidth, innerHeight);

        for (let i = 0; i < particlesArray.length; i++) {
            particlesArray[i].update();
        }
        connect();
    }
    createParticle.init = init;
    init();
    animate();
}

//reszie event
window.addEventListener('resize',
    function () {
        canvas.width = innerWidth;
        canvas.height = innerHeight;
        mouse.radius = ((canvas.height / 80) * (canvas.height / 80));
        createParticle.init();
    }
)

//mouse out event
window.addEventListener('mouseout',
    function () {
        mouse.x = undefined;
        mouse.y = undefined;
    }
)