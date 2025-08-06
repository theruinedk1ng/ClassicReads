document.addEventListener('DOMContentLoaded', () => {
  const urlsToPreview = [
    'https://www.goodreads.com/list/show/1599.Best_Philosophical_Fiction',
    'https://www.goodreads.com/list/show/449.Must_Read_Classics',
    'https://www.goodreads.com/list/show/26495.Best_Woman_Authored_Books'
  ];

  const container = document.getElementById('preview2');

  urlsToPreview.forEach(url => {
    const apiUrl = `https://api.microlink.io/?url=${encodeURIComponent(url)}`;

    fetch(apiUrl)
      .then(response => response.json())
      .then(data => {
        if (data.status === 'success') {
          const preview = data.data;

          const link = document.createElement('a');
          link.href = preview.url;
          link.target = '_blank';
          link.className = 'preview-link';

          const wrapper = document.createElement('div');
          wrapper.className = 'link-preview';

          const img = document.createElement('img');
          img.src = preview.image?.url || '';
          img.alt = 'Preview Image';

          const content = document.createElement('div');
          content.className = 'preview-content';

          const title = document.createElement('h3');
          title.textContent = preview.title;

          const desc = document.createElement('p');
          desc.textContent = preview.description;

          content.appendChild(title);
          content.appendChild(desc);
          wrapper.appendChild(img);
          wrapper.appendChild(content);
          link.appendChild(wrapper);

          container.appendChild(link);

        } else {
          const errorMsg = document.createElement('p');
          errorMsg.textContent = 'Failed to load preview.';
          container.appendChild(errorMsg);
        }
      })
      .catch(() => {
        const errorMsg = document.createElement('p');
        errorMsg.textContent = 'Error loading preview.';
        container.appendChild(errorMsg);
      });
  });
});
