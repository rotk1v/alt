fetch("../results/results-all.json")
    .then((response) => response.json())
    .then((jsonData) => {
        var myDiv = document.getElementById("container");

        jsonData /* .slice(0, 10) */
            .forEach((item) => {
                var container = document.createElement("div");
                container.className = "item-container";

                var title = document.createElement("span");
                title.innerText = item.title;

                var url = document.createElement("a");
                url.href = item.url;
                // url.innerText = item.url.split("/")[2];
                url.target = "_blank";

                var preview = document.createElement("img");
                preview.className = "article-preview";
                if (item.previewUrl != "") preview.src = item.previewUrl;
                url.appendChild(preview);

                var source = document.createElement("h2");
                source.innerText = item.source;

                container.appendChild(title);
                container.appendChild(url);
                container.appendChild(source);
                myDiv.appendChild(container);
            });
    })
    .catch((error) => console.error(error));
