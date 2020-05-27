<script src="https://cdn.jsdelivr.net/npm/fuse.min.js@6.0.0"></script>

<script type="text/javascript">
fetch('/search.json')
  .then(function (response) {
    return response.json();
  })
  .then(function (data) {
    appendData(data);
    console.log(data)
  })
  .catch(function (err) {
    console.log(err);
  });

const options = {
  // isCaseSensitive: false,
  // includeScore: false,
  // shouldSort: true,
  // includeMatches: false,
  // findAllMatches: false,
  // minMatchCharLength: 1,
  // location: 0,
  // threshold: 0.6,
  // distance: 100,
  // useExtendedSearch: false,
  // keys: [],
};

const fuse = new Fuse(data, options);

// Change the pattern
const pattern = ""

return fuse.search(pattern)
</script>

