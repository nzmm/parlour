<script lang="ts">
  let className = "";

  export { className as class };
  export let placement = "fixed-top";
</script>

<nav class="navbar {placement} navbar-expand-lg navbar-light bg-light {className}">
  <slot></slot>
</nav>
